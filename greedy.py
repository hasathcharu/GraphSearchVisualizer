import queue
import networkx as nx
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
