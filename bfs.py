import queue

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