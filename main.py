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

# def dfs(graph,start_node, end_node, visited=None):
#   if (visited is None):
#     visited = set()
#   visited.add(start_node)
#   if(start_node == end_node):
#     return [start_node]
#   order = []
#   for node in graph[start_node]:
#     if node not in visited:
#       order = dfs(graph,node,end_node,visited)
#       if order is not None:
#         order.insert(0,start_node)
#   return order

def dfs(graph, start_node, end_node, visited=set()):
  order=[]
  if start_node not in visited:
    order.append(start_node)
    visited.add(start_node)
    for node in graph[start_node]:
      if node not in visited:
        order.extend(dfs(graph,node,visited))
      if(end_node in order):
        break

  return order

def dls(graph, start_node, end_node, limit=1,visited=set(),level=0):
  order=[]
  if(level == limit):
    return [start_node]
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

def get_node_color(node, order, end_node, graph, final=False):
  color_map = []
  if(len(order) == 0):
    return 'b'
  for i in graph.nodes:
    color = 'b'
    if i == node:
      color='y'
    if i in order and final:
      color='purple'
    if i == end_node:
      color='g'
    if i == order[0]:
      color='r'
    color_map.append(color)
  return color_map

def visualize_search(order,title, G, position, end_node):
  print(order)
  plt.figure() 
  plt.title(title)
  for i, node in enumerate(order, start=1):
    plt.clf()
    plt.title(title)
    nx.draw(G, position, with_labels=True, node_color=get_node_color(node, order, end_node, G))
    plt.draw()
    plt.pause(1)

  nx.draw(G, position, with_labels=True, node_color=get_node_color(node, order, end_node, G,True))
  plt.draw()


  plt.show()

def visualize_idls_search(start_node, end_node,title, G, position):
  plt.figure() 
  plt.title(title)
  order = []
  for j in range(1,10):
    order.extend(dls(G, start_node, end_node, limit=j,visited=set()))
    if(end_node in order):
      break
  print(order)
  for i, node in enumerate(order, start=1):
    plt.clf()
    plt.title(title)
    nx.draw(G, position, with_labels=True, node_color=get_node_color(node, order, end_node, G))
    plt.draw()
    plt.pause(1)

  nx.draw(G, position, with_labels=True, node_color=get_node_color(node, order, end_node, G,True))
  plt.draw()


  plt.show()



G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 8),(2, 4), (3, 5), (4, 6), (6,7)])
# G.add_edges_from([('S','A'), ('S','R'), ('S','P'), ('A','Q'),('A','O'),('R','U'),('R','V'),('R','W'),('P','M'),('Q','W'),('W','G')])
G.add_edges_from([
  ('Haritha','Manupa',{'weight':3}),
  ('Haritha','Ransilu',{'weight':1}),
  ('Haritha','Waruni',{'weight':5}),
  ('Haritha','Menura',{'weight':4}),
  ('Manupa','Isuri',{'weight':1}),
  ('Ransilu','Thathsarani',{'weight':2}),
  ('Ransilu','Kithmi',{'weight':4}),
  ('Ransilu','Ranul',{'weight':5}),
  ('Waruni','Menura',{'weight':1}),
  ('Menura','Ranul',{'weight':3}),
  ('Isuri','Kithmi',{'weight':3}),
  ('Isuri','Rashmi',{'weight':1}),
  ('Isuri','Thathsarani',{'weight':5}),
  ('Kithmi','Rashmi',{'weight':5}),
  ('Ranul','Taneesha',{'weight':1}),
  ('Taneesha','Rashmi',{'weight':2}),
])
pos = nx.spring_layout(G)

def get_path(start,order, graph):
  path = []
  path.append(start)
  for i in range(1,len(order)-1):
    if(order[i] in graph.neighbors(path[-1])):
      path.append(order[i])
  path.append(order[-1])
  return path

# visualize_search(bfs(G, 'Haritha', 'Rashmi'), "BFS Visualization", G, pos, 'Rashmi')
# visualize_search(dfs(G, 'Haritha', 'Rashmi'), "DFS Visualization", G, pos, 'Rashmi')
# visualize_search(dls(G, 'S', 'G',2), "DLS Visualization", G, pos, 'G')
# visualize_idls_search('S', 'G', "IDLS Visualization", G, pos)