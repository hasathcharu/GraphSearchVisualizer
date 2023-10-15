import queue
import networkx as nx
import matplotlib.pyplot as plt


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
  if(level == limit):
    return []
  if start_node not in visited:
    order.append(start_node)
    visited.add(start_node)
    for node in graph[start_node]:
      if node not in visited:
        order.extend(dls(graph,node,end_node,limit,visited, level+1))
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
    print('processing', vertex)
    print(q.queue)
    if vertex not in visited:
      visited.add(vertex[2])
      order.append(vertex[2])
      for node in graph[vertex[2]]:
        if node not in visited and all(node != item[2] for item in q.queue):
          entry_counter+=1
          curr_cost = graph[vertex[2]][node]['weight'] + vertex[0] - nx.get_node_attributes(graph, 'h')[vertex[2]]
          if(vertex[1]==0):
            curr_cost = graph[vertex[2]][node]['weight']
          print('vertex', vertex, 'node', node, 'curr_cost', curr_cost)

          h = nx.get_node_attributes(graph, 'h')[node]
          q.put((curr_cost+h, entry_counter, node))
          print('queue', q.queue)
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
  print(order)
  plt.figure() 
  plt.title(title)
  legend_colors = {'Not Visited': '#6ec2f7', 'Currently Visiting / Path': '#fffaa0', 'Visited': '#a686fc', 'Start Node': '#ff7276', 'Goal Node': '#7adc7a'}
  legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, label=label, markersize=15) for label, color in legend_colors.items()]
  plt.clf()
  plt.pause(3)
  for i, node in enumerate(order, start=1):
    plt.clf()
    plt.title(title)
    nx.draw(G, position, with_labels=True,node_color=get_node_color(node, order, end_node, G), node_size=5000)
    edge_labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_labels(G, {node: (x, y-0.2) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()}, labels=nx.get_node_attributes(G, 'h'))
    nx.draw_networkx_edge_labels(G,position,edge_labels=edge_labels)
    plt.legend(handles=legend_elements, loc='lower right')

    plt.draw()
    plt.pause(1)

  node=None
  nx.draw(G, position, with_labels=True, node_color=get_node_color(node, order, end_node, G,True, backtrack_path(order[0],end_node, order, G)),node_size=5000)
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
  plt.title(title)
  legend_colors = {'Not Visited': '#6ec2f7', 'Currently Visiting / Path': '#fffaa0', 'Visited': '#a686fc', 'Start Node': '#ff7276', 'Goal Node': '#7adc7a'}
  legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, label=label, markersize=15) for label, color in legend_colors.items()]
  plt.clf()
  plt.pause(3)
  order = []
  for j in range(1,10):
    order = dls(G, start_node, end_node, limit=j,visited=set())
    for i, node in enumerate(order, start=1):
      plt.clf()
      plt.title(title)
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

  nx.draw(G, position, with_labels=True, node_color=get_node_color(node, order, end_node, G,True, backtrack_path(order[0],end_node, order, G)),node_size=5000)
  plt.draw()
  plt.show()



G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 8),(2, 4), (3, 5), (4, 6), (6,7)])
# G.add_edges_from([('S','A'), ('S','R'), ('S','P'), ('A','Q'),('A','O'),('R','U'),('R','V'),('R','W'),('P','M'),('Q','W'),('W','G')])
G.add_edges_from([
  ('Haritha','Manupa',{'weight':3}),
  ('Haritha','Ransilu',{'weight':1}),
  ('Haritha','Waruni',{'weight':5}),
  ('Haritha','Menura',{'weight':4, }),
  ('Manupa','Isuri',{'weight':1, }),
  ('Ransilu','Thathsarani',{'weight':2, }),
  ('Ransilu','Kithmi',{'weight':4, }),
  ('Ransilu','Ranul',{'weight':5, }),
  ('Waruni','Menura',{'weight':1, }),
  ('Menura','Ranul',{'weight':3, }),
  ('Isuri','Rashmi',{'weight':1, }),
  ('Isuri','Kithmi',{'weight':3, }),
  ('Isuri','Thathsarani',{'weight':5, }),
  ('Kithmi','Rashmi',{'weight':5, }),
  ('Ranul','Taneesha',{'weight':1, }),
  ('Taneesha','Rashmi',{'weight':2, }),
  # ('Taneesha','Rashmi',{'weight':1, }),
])
G.nodes['Haritha']['pos'] = (3.5, 2)
G.nodes['Manupa']['pos'] = (2.5, 1)
G.nodes['Ransilu']['pos'] = (3.2, 1)
G.nodes['Waruni']['pos'] = (4, 1)
G.nodes['Menura']['pos'] = (4.5, 2)
G.nodes['Isuri']['pos'] = (2.5, -1)
G.nodes['Kithmi']['pos'] = (3.5, -1)
G.nodes['Ranul']['pos'] = (4.5, 0)
G.nodes['Taneesha']['pos'] = (4, -1.5)
G.nodes['Rashmi']['pos'] = (3.5, -3)
G.nodes['Thathsarani']['pos'] = (3, 0)

G.nodes['Haritha']['h'] = 10
G.nodes['Manupa']['h'] = 6
G.nodes['Ransilu']['h'] = 5
G.nodes['Waruni']['h'] = 7
G.nodes['Menura']['h'] = 9
G.nodes['Isuri']['h'] = 1
G.nodes['Kithmi']['h'] = 2
G.nodes['Ranul']['h'] = 4
# G.nodes['Taneesha']['h'] = 1
G.nodes['Taneesha']['h'] = 3
G.nodes['Rashmi']['h'] = 0
G.nodes['Thathsarani']['h'] = 8

pos = {node: (x, y) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()}


# visualize_search(bfs(G, 'Haritha', 'Rashmi'), "BFS Visualization", G, pos, 'Rashmi')
# visualize_search(dfs(G, 'Haritha', 'Rashmi'), "DFS Visualization", G, pos, 'Rashmi')
# visualize_search(dls(G, 'Haritha', 'Rashmi',3), "DLS Visualization", G, pos, 'Rashmi')
# visualize_idls_search('Haritha', 'Rashmi', "IDLS Visualization", G, pos)
# visualize_search(ucs(G, 'Haritha', 'Rashmi'), "UCS Visualization", G, pos, 'Rashmi')
# visualize_search(greedy(G, 'Haritha', 'Rashmi'), "Greedy Visualization", G, pos, 'Rashmi')
# visualize_search(a_star(G, 'Haritha', 'Rashmi'), "A Star Visualization", G, pos, 'Rashmi')


print("Select Algorithm")
print("1. Breadth First Search")
print("2. Depth First Search")
print("3. Depth Limited Search")
print("4. Iterative Deepening Search")
print("5. Uniform Cost Search")
print("6. Greedy Search")
print("7. A* Search")

choice = int(input("Enter your choice: "))
if choice==1:
  visualize_search(bfs(G, 'Haritha', 'Rashmi'), "Breadth First Search Visualization", G, pos, 'Rashmi')
elif choice==2:
  visualize_search(dfs(G, 'Haritha', 'Rashmi'), "Depth First Search Visualization", G, pos, 'Rashmi')
elif choice==3:
  visualize_search(dls(G, 'Haritha', 'Rashmi',3), "Depth Limited Search Visualization", G, pos, 'Rashmi')
elif choice==4:
  visualize_idls_search('Haritha', 'Rashmi', "Iterative Deepening Search Visualization", G, pos)
elif choice==5:
  visualize_search(ucs(G, 'Haritha', 'Rashmi'), "Uniform Cost Search Visualization", G, pos, 'Rashmi')
elif choice==6:
  visualize_search(greedy(G, 'Haritha', 'Rashmi'), "Greedy Search Visualization", G, pos, 'Rashmi')
elif choice==7:
  visualize_search(a_star(G, 'Haritha', 'Rashmi'), "A Star Search Visualization", G, pos, 'Rashmi')
