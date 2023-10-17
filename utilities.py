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
      color='#9bfdcc'
    if i == order[0]:
      color='#ff7276'
    if i == node:
      color='#fffaa0'
    color_map.append(color)
  return color_map

def draw_copyright_text(G=None):
  x = 0.5
  y = -1
  if (G):
    positions = [(x, y) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()]
    x = sum([x for (x,y) in positions])/len(positions)
    y = min([y for (x,y) in positions])-1.3
  plt.text(x, y, "Made with ❤️ by Haritha Hasathcharu", color='#eeeeee', ha='center')

def draw_graph(title, text_content, position, edge_labels, legend_elements,G, node, order, end_node, final=False, path=[]):
  plt.gcf().clf()
  plt.suptitle(title, color='#eeeeee')
  plt.text(2.5, -4, text_content, color='#eeeeee')
  nx.draw(G, position, with_labels=True,node_color=get_node_color(node, order, end_node, G, final, path), node_size=5000, edge_color='#eeeeee')
  nx.draw_networkx_labels(G, {node: (x, y-0.2) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()}, labels=nx.get_node_attributes(G, 'h'), font_color='#333333')
  nx.draw_networkx_edge_labels(G,position,edge_labels=edge_labels, font_color='#333333')
  legend = plt.legend(handles=legend_elements, loc='lower right')
  legend.get_frame().set_facecolor('#111111')  
  legend.get_frame().set_linewidth(0)
  legend.get_frame().set_edgecolor('none')
  for text in legend.get_texts():
    text.set_color('#eeeeee')
  draw_copyright_text(G)
  plt.gcf().set_facecolor('#111111')
  plt.gca().set_facecolor('#111111')
  plt.draw()



def get_text(order,path):
  path_text = (', ').join(path[i] for i in range(len(path)-1, -1, -1))
  if(len(path_text) == 0):
    path_text = 'No path found'
                          
  return 'Traversal: ' + (', ').join(order) + '\nPath: ' + path_text