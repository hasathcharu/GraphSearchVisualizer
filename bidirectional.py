import queue
from graph import G
def bidirectional(graph, start_node, end_node):
  visited = set()
  sq = queue.Queue()
  eq = queue.Queue()
  sq.put(start_node)
  eq.put(end_node)
  sorder = []
  eorder = []
  while not (sq.empty() and eq.empty()):
    svertex = ''
    evertex = ''
    if(not sq.empty() and not eq.empty()):
      svertex = sq.get()
      evertex = eq.get()
    elif(sq.empty()):
      evertex = eq.get()
    elif(eq.empty()):
      svertex = sq.get()


    if svertex in eorder:
      ueorder = eorder [:eorder.index(svertex)+1]
      order = sorder.copy()
      order.extend(ueorder[::-1])
      break
    if evertex in sorder:
      usorder = sorder [:sorder.index(evertex)+1]
      order = usorder.copy()
      order.extend(eorder[::-1])
      break
    if (svertex and svertex not in visited):
      visited.add(svertex)
      sorder.append(svertex)

      for node in graph[svertex]:
        if node not in visited:
          sq.put(node)
          

    if (evertex and evertex not in visited):
      visited.add(evertex)
      eorder.append(evertex)
      for node in graph[evertex]:
        if node not in visited:
          eq.put(node)
          
  return sorder, eorder, order

# print(bidirectional(G, 'Haritha', 'Rashmi'))