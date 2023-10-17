import matplotlib.pyplot as plt
import networkx as nx
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

def draw_graph_background(title, text_pos, text_content, position, edge_labels, legend_elements,G):
  plt.title(title)
  plt.text(text_pos[0], text_pos[1], text_content, color='#333333')
  nx.draw_networkx_labels(G, {node: (x, y-0.2) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()}, labels=nx.get_node_attributes(G, 'h'))
  nx.draw_networkx_edge_labels(G,position,edge_labels=edge_labels)
  plt.legend(handles=legend_elements, loc='lower right')


def get_text(order,path):
  path_text = (', ').join(path[i] for i in range(len(path)-1, -1, -1))
  if(len(path_text) == 0):
    path_text = 'No path found'
                          
  return 'Traversal: ' + (', ').join(order) + '\nPath: ' + path_text