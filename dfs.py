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