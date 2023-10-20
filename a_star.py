import queue
import networkx as nx
def a_star(graph, start_node, end_node):
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
        curr_cost = graph[vertex[2]][node]['weight'] + vertex[0] - nx.get_node_attributes(graph, 'h')[vertex[2]]
        if(vertex[1]==0):
          curr_cost = graph[vertex[2]][node]['weight']
        h = nx.get_node_attributes(graph, 'h')[node]
        if node not in visited:
          if all(node != item[2] for item in q.queue):
            entry_counter+=1
            q.put((curr_cost+h, entry_counter, node))
          else:
            for item in q.queue:
              if item[2] == node:
                if curr_cost + h < item[0]:
                  entry_counter+=1
                  q.queue.remove(item)
                  q.put((curr_cost+h, entry_counter, node))
    if vertex[2] == end_node:
      break
  return order