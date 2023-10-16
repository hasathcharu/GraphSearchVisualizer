import queue
import networkx as nx
import matplotlib.pyplot as plt
from graph import G
from matplotlib.widgets import Button


def bfs(graph, start_node, end_node):
  visited = set()
  q = queue.Queue()
  q.put(start_node)
  order = []
  path = []
  while not q.empty():
    vertex = q.get()
    if vertex not in visited:
      visited.add(vertex)
      order.append(vertex)
      for node in graph[vertex]:
        if node not in visited:
          q.put(node)
      if vertex == end_node:
        break
  return order



def dfs(graph, start_node, end_node, visited=set()):
  if visited is None:
    visited = set()
  order=[]
  if start_node not in visited:
    order.append(start_node)
    visited.add(start_node)
    for node in graph[start_node]:
      if node not in visited:
        order.extend(dfs(graph,node,end_node,visited))
      if(end_node in order):
        break
  return order

def dls(graph, start_node, end_node, limit=1,visited=set(),level=0):
  order=[]
  if(level > limit):
    return []
  if start_node not in visited:
    order.append(start_node)
    visited.add(start_node)
    for node in graph[start_node]:
      # print('start_node', start_node, 'node', node, 'level', level)
      if node not in visited:
        if(level+1==limit) and node not in order:
          order.append(node)
        else:
          new_order = dls(graph,node,end_node,limit,visited, level+1)
          for sub_node in new_order:
            if sub_node not in order:
              order.append(sub_node)
      if(end_node in order):
        break

  return order

def ucs(graph, start_node, end_node):
  visited = set()
  q = queue.PriorityQueue()
  entry_counter =0
  q.put((0,entry_counter,start_node))
  
  order = []
  while not q.empty():
    vertex = q.get()
    if vertex not in visited:
      visited.add(vertex[2])
      order.append(vertex[2])
      for node in graph[vertex[2]]:
        if node not in visited and all(node != item[2] for item in q.queue):
          entry_counter+=1
          q.put((graph[vertex[2]][node]['weight']+vertex[0],entry_counter, node))
    if vertex[2] == end_node:
      break
  return order

def greedy(graph, start_node, end_node):
  visited = set()
  q = queue.Queue()
  q.put(start_node)
  
  order = []
  while not q.empty():
    vertex = q.get()
    if vertex not in visited:
      visited.add(vertex)
      order.append(vertex)
      min = None
      min_heuristic = 100
      for node in graph[vertex]:
        h = nx.get_node_attributes(graph, 'h')[node]
        if h < min_heuristic:
          min = node
          min_heuristic = h
      if min is not None and min not in visited:      
        q.put(min)    
    if vertex == end_node:
      break
  return order

def a_star(graph, start_node, end_node):
  visited = set()
  q = queue.PriorityQueue()
  entry_counter =0
  q.put((0,entry_counter,start_node))
  
  order = []
  while not q.empty():
    vertex = q.get()
    # print('processing', vertex)
    if vertex not in visited:
      visited.add(vertex[2])
      order.append(vertex[2])
      for node in graph[vertex[2]]:
        curr_cost = graph[vertex[2]][node]['weight'] + vertex[0] - nx.get_node_attributes(graph, 'h')[vertex[2]]
        if(vertex[1]==0):
          curr_cost = graph[vertex[2]][node]['weight']
        h = nx.get_node_attributes(graph, 'h')[node]
        if node not in visited:
          if all(node != item[2] for item in q.queue):
            entry_counter+=1
            # print('vertex', vertex, 'node', node, 'curr_cost', curr_cost)
            q.put((curr_cost+h, entry_counter, node))
          else:
            for item in q.queue:
              if item[2] == node:
                if curr_cost + h < item[0]:
                  # print('vertex', vertex, 'node', node, 'curr_cost', curr_cost)
                  entry_counter+=1
                  q.queue.remove(item)
                  q.put((curr_cost+h, entry_counter, node))
          # print('queue', q.queue)
    if vertex[2] == end_node:
      break
  return order

def get_node_color(node, order, end_node, graph, final=False, path=[]):
  color_map = []
  if(len(order) == 0):
    return 'b'
  for i in graph.nodes:
    color = '#6ec2f7'

    if i in order and final:
      color='#a686fc'
    if i in path:
      color='#fffaa0'
    if i == end_node:
      color='#7adc7a'
    if i == order[0]:
      color='#ff7276'
    if i == node:
      color='#fffaa0'
    color_map.append(color)
  return color_map

def visualize_search(order,title, G, position, end_node):
  plt.figure() 
  text_x = 2.5
  text_y = -4
  path = backtrack_path(order[0],end_node, order, G)
  text_content = 'Traversal: ' + (', ').join(order) + '\nPath: ' + (', ').join(path[i] for i in range(len(path)-1, -1, -1))
  print('Traversal', order)
  print('Path', path)
  plt.title(title)
  plt.text(text_x, text_y, text_content, color='#333333')
  legend_colors = {'Not Visited': '#6ec2f7', 'Currently Visiting / Path': '#fffaa0', 'Visited': '#a686fc', 'Start Node': '#ff7276', 'Goal Node': '#7adc7a'}
  legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, label=label, markersize=15) for label, color in legend_colors.items()]
  plt.clf()
  # plt.pause(3)
  for i, node in enumerate(order, start=1):
    plt.clf()
    plt.title(title)
    plt.text(text_x, text_y, text_content, color='#333333')
    nx.draw(G, position, with_labels=True,node_color=get_node_color(node, order, end_node, G), node_size=5000)
    edge_labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_labels(G, {node: (x, y-0.2) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()}, labels=nx.get_node_attributes(G, 'h'))
    nx.draw_networkx_edge_labels(G,position,edge_labels=edge_labels)
    plt.legend(handles=legend_elements, loc='lower right')

    plt.draw()
    plt.pause(1)

  node=None
  plt.clf()
  plt.title(title)
  plt.text(text_x, text_y, text_content, color='#333333')
  nx.draw(G, position, with_labels=True, node_color=get_node_color(node, order, end_node, G,True, path),node_size=5000)
  edge_labels = nx.get_edge_attributes(G,'weight')
  nx.draw_networkx_labels(G, {node: (x, y-0.2) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()}, labels=nx.get_node_attributes(G, 'h'))
  nx.draw_networkx_edge_labels(G,position,edge_labels=edge_labels)
  plt.legend(handles=legend_elements, loc='lower right')
  plt.draw()
  plt.show()

def backtrack_path(start_node, end_node, order, graph):
  if(end_node not in order):
    return []
  path = []
  path.append(end_node)
  for i in range(len(order)-1,0,-1):
    if(order[i] in graph.neighbors(path[-1])):
      path.append(order[i])
  path.append(start_node)
  return path

def visualize_idls_search(start_node, end_node,title, G, position):
  plt.figure() 
  text_x = 2
  text_y = 2
  text_content = 'Depth Limit: '
  plt.title(title)
  legend_colors = {'Not Visited': '#6ec2f7', 'Currently Visiting / Path': '#fffaa0', 'Visited': '#a686fc', 'Start Node': '#ff7276', 'Goal Node': '#7adc7a'}
  legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, label=label, markersize=15) for label, color in legend_colors.items()]
  plt.clf()
  plt.pause(3)
  plt.text(text_x, text_y, text_content, fontsize=12, color='red')
  order = []
  for j in range(1,10):
    order = dls(G, start_node, end_node, limit=j,visited=set())
    print(order)
    for i, node in enumerate(order, start=1):
      plt.clf()
      plt.title(title)
      plt.text(text_x, text_y, text_content, fontsize=12, color='red')
      nx.draw(G, position, with_labels=True,node_color=get_node_color(node, order, end_node, G), node_size=5000)
      edge_labels = nx.get_edge_attributes(G,'weight')
      nx.draw_networkx_labels(G, {node: (x, y-0.2) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()}, labels=nx.get_node_attributes(G, 'h'))
      nx.draw_networkx_edge_labels(G,position,edge_labels=edge_labels)
      plt.legend(handles=legend_elements, loc='lower right')
      plt.draw()
      plt.pause(1)
    if(end_node in order):
      break
  node = None
  plt.clf()
  plt.clf()
  plt.title(title)
  plt.text(text_x, text_y, text_content, color='#333333')
  nx.draw(G, position, with_labels=True, node_color=get_node_color(node, order, end_node, G,True, backtrack_path(order[0],end_node, order, G)),node_size=5000)
  edge_labels = nx.get_edge_attributes(G,'weight')
  nx.draw_networkx_labels(G, {node: (x, y-0.2) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()}, labels=nx.get_node_attributes(G, 'h'))
  nx.draw_networkx_edge_labels(G,position,edge_labels=edge_labels)
  plt.legend(handles=legend_elements, loc='lower right')
  plt.draw()
  plt.show()




pos = {node: (x, y) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()}


# visualize_search(bfs(G, 'Haritha', 'Rashmi'), "BFS Visualization", G, pos, 'Rashmi')
# visualize_search(dfs(G, 'Haritha', 'Rashmi'), "DFS Visualization", G, pos, 'Rashmi')
# visualize_search(dls(G, 'Haritha', 'Rashmi',3), "DLS Visualization", G, pos, 'Rashmi')
# visualize_idls_search('Haritha', 'Rashmi', "IDLS Visualization", G, pos)
# visualize_search(ucs(G, 'Haritha', 'Rashmi'), "UCS Visualization", G, pos, 'Rashmi')
# visualize_search(greedy(G, 'Haritha', 'Rashmi'), "Greedy Visualization", G, pos, 'Rashmi')
# visualize_search(a_star(G, 'Haritha', 'Rashmi'), "A Star Visualization", G, pos, 'Rashmi')

def on_bfs_button_click(event):
  visualize_search(bfs(G, 'Haritha', 'Rashmi'), "Breadth First Search Visualization", G, pos, 'Rashmi')

def on_dfs_button_click(event):
  visualize_search(dfs(G, 'Haritha', 'Rashmi'), "Depth First Search Visualization", G, pos, 'Rashmi')

def on_depth1_button_click(event):
  visualize_search(dls(G, 'Haritha', 'Rashmi',1), "Depth Limited Search Visualization - Depth 1", G, pos, 'Rashmi')

def on_depth2_button_click(event):
  visualize_search(dls(G, 'Haritha', 'Rashmi',2), "Depth Limited Search Visualization - Depth 2", G, pos, 'Rashmi')

def on_depth3_button_click(event):
  visualize_search(dls(G, 'Haritha', 'Rashmi',3), "Depth Limited Search Visualization - Depth 3", G, pos, 'Rashmi')

def on_depth4_button_click(event):
  visualize_search(dls(G, 'Haritha', 'Rashmi',4), "Depth Limited Search Visualization - Depth 4", G, pos, 'Rashmi')

def on_depth5_button_click(event):
  visualize_search(dls(G, 'Haritha', 'Rashmi',5), "Depth Limited Search Visualization - Depth 5", G, pos, 'Rashmi')

def on_depth6_button_click(event):
  visualize_search(dls(G, 'Haritha', 'Rashmi',6), "Depth Limited Search Visualization - Depth 6", G, pos, 'Rashmi')

def on_dls_button_click(event):
  plt.figure()
  plt.clf()
  plt.title("Select Depth Limit")
  d1_button = Button(plt.axes([0.25, 0.75, 0.5, 0.075]), 'Depth 1')
  d2_button = Button(plt.axes([0.25, 0.655, 0.5, 0.075]), 'Depth 2')
  d3_button = Button(plt.axes([0.25, 0.56, 0.5, 0.075]), 'Depth 3')
  d4_button = Button(plt.axes([0.25, 0.465, 0.5, 0.075]), 'Depth 4')
  d5_button = Button(plt.axes([0.25, 0.37, 0.5, 0.075]), 'Depth 5')
  d6_button = Button(plt.axes([0.25, 0.275, 0.5, 0.075]), 'Depth 6')
  d1_button.on_clicked(on_depth1_button_click)
  d2_button.on_clicked(on_depth2_button_click)
  d3_button.on_clicked(on_depth3_button_click)
  d4_button.on_clicked(on_depth4_button_click)
  d5_button.on_clicked(on_depth5_button_click)
  d6_button.on_clicked(on_depth6_button_click)
  # plt.draw()

def on_idls_button_click(event):
  visualize_idls_search('Haritha', 'Rashmi', "Iterative Deepening Search Visualization", G, pos)

def on_ucs_button_click(event):
  visualize_search(ucs(G, 'Haritha', 'Rashmi'), "Uniform Cost Search Visualization", G, pos, 'Rashmi')

def on_greedy_button_click(event):
  visualize_search(greedy(G, 'Haritha', 'Rashmi'), "Greedy Search Visualization", G, pos, 'Rashmi')

def on_a_star_button_click(event):
  visualize_search(a_star(G, 'Haritha', 'Rashmi'), "A Star Search Visualization", G, pos, 'Rashmi')


def main():
  plt.clf()
  bfs_button_ax = plt.axes([0.25, 0.75, 0.5, 0.075])
  dfs_button_ax = plt.axes([0.25, 0.655, 0.5, 0.075])
  dls_button_ax = plt.axes([0.25, 0.56, 0.5, 0.075])
  idls_button_ax = plt.axes([0.25, 0.465, 0.5, 0.075])
  ucs_button_ax = plt.axes([0.25, 0.37, 0.5, 0.075])
  greedy_button_ax = plt.axes([0.25, 0.275, 0.5, 0.075])
  a_star_button_ax = plt.axes([0.25, 0.18, 0.5, 0.075])
  bfs_button = Button(bfs_button_ax, 'Breadth First Search')
  dfs_button = Button(dfs_button_ax, 'Depth First Search')
  dls_button = Button(dls_button_ax, 'Depth Limited Search')
  idls_button = Button(idls_button_ax, 'Iterative Deepening Search')
  ucs_button = Button(ucs_button_ax, 'Uniform Cost Search')
  greedy_button = Button(greedy_button_ax, 'Greedy Search')
  a_star_button = Button(a_star_button_ax, 'A* Search')
  bfs_button.on_clicked(on_bfs_button_click)
  dfs_button.on_clicked(on_dfs_button_click)
  dls_button.on_clicked(on_dls_button_click)
  idls_button.on_clicked(on_idls_button_click)
  ucs_button.on_clicked(on_ucs_button_click)
  greedy_button.on_clicked(on_greedy_button_click)
  a_star_button.on_clicked(on_a_star_button_click)
  plt.show()
  # print("Select Algorithm")
  # print("1. Breadth First Search")
  # print("2. Depth First Search")
  # print("3. Depth Limited Search")
  # print("4. Iterative Deepening Search")
  # print("5. Uniform Cost Search")
  # print("6. Greedy Search")
  # print("7. A* Search")
  
  # choice = int(input("Enter your choice: "))
  # if choice==1:
  #   visualize_search(bfs(G, 'Haritha', 'Rashmi'), "Breadth First Search Visualization", G, pos, 'Rashmi')
  # elif choice==2:
  #   visualize_search(dfs(G, 'Haritha', 'Rashmi'), "Depth First Search Visualization", G, pos, 'Rashmi')
  # elif choice==3:
  #   visualize_search(dls(G, 'Haritha', 'Rashmi',int(input("Enter Depth: "))), "Depth Limited Search Visualization", G, pos, 'Rashmi')
  # elif choice==4:
  #   visualize_idls_search('Haritha', 'Rashmi', "Iterative Deepening Search Visualization", G, pos)
  # elif choice==5:
  #   visualize_search(ucs(G, 'Haritha', 'Rashmi'), "Uniform Cost Search Visualization", G, pos, 'Rashmi')
  # elif choice==6:
  #   visualize_search(greedy(G, 'Haritha', 'Rashmi'), "Greedy Search Visualization", G, pos, 'Rashmi')
  # elif choice==7:
  #   visualize_search(a_star(G, 'Haritha', 'Rashmi'), "A Star Search Visualization", G, pos, 'Rashmi')

main()