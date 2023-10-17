
import queue
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