import queue
import networkx as nx
import matplotlib.pyplot as plt
from graph import G
from matplotlib.widgets import Button
from bfs import bfs
from dfs import dfs
from dls import dls
from ucs import ucs
from greedy import greedy
from a_star import a_star
from utilities import get_node_color
from utilities import draw_graph_background
from utilities import get_text
from backtrack import backtrack_path

start = 'Haritha'
end = 'Rashmi'
text_pos = (2.5, -4)
legend_colors = {'Not Visited': '#6ec2f7', 'Currently Visiting / Path': '#fffaa0', 'Visited': '#a686fc', 'Start Node': '#ff7276', 'Goal Node': '#7adc7a'}
btn_color = '#7adc7a'
btn_hover_color = '#5da65d'
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, label=label, markersize=15) for label, color in legend_colors.items()]
edge_labels = nx.get_edge_attributes(G,'weight')
pos = {node: (x, y) for node, (x, y) in nx.get_node_attributes(G, 'pos').items()}

figures = []

def visualize_search(order,title, G, position, end_node):
  path = backtrack_path(order[0],end_node, order, G)
  print('Traversal', order)
  print('Path', path)
  plt.figure() 
  plt.clf()
  draw_graph_background(title, text_pos, get_text(order,path), position, edge_labels, legend_elements,G)
  for i, node in enumerate(order, start=1):
    plt.clf()
    draw_graph_background(title, text_pos, get_text(order,path), position, edge_labels, legend_elements,G)
    nx.draw(G, position, with_labels=True,node_color=get_node_color(node, order, end_node, G), node_size=5000)
    plt.draw()
    plt.pause(1)

  node=None
  plt.clf()
  draw_graph_background(title, text_pos, get_text(order,path), position, edge_labels, legend_elements,G)
  nx.draw(G, position, with_labels=True, node_color=get_node_color(node, order, end_node, G,True, path),node_size=5000)
  plt.draw()
  plt.show()



def visualize_idls_search(start_node, end_node,title, G, position):
  plt.figure() 
  path = None
  plt.clf()
  order = []
  for j in range(1,10):
    order = dls(G, start_node, end_node, limit=j,visited=set())
    path = backtrack_path(order[0],end_node, order, G)
    for i, node in enumerate(order, start=1):
      plt.clf()
      draw_graph_background(title + '\n\nDepth '+str(j), text_pos, get_text(order,path), position, edge_labels, legend_elements,G)
      nx.draw(G, position, with_labels=True,node_color=get_node_color(node, order, end_node, G), node_size=5000)
      plt.draw()
      plt.pause(1)
    
    if(end_node in order):
      break
  node = None
  plt.clf()
  draw_graph_background(title + '\n\nDepth '+str(j), text_pos, get_text(order,path), position, edge_labels, legend_elements,G)
  nx.draw(G, position, with_labels=True, node_color=get_node_color(node, order, end_node, G,True, backtrack_path(order[0],end_node, order, G)),node_size=5000)
  plt.draw()
  plt.show()


def on_bfs_button_click(event):
  visualize_search(bfs(G, start, end), "Breadth First Search Visualization", G, pos, end)

def on_dfs_button_click(event):
  visualize_search(dfs(G, start, end), "Depth First Search Visualization", G, pos, end)

def on_depth1_button_click(event):
  visualize_search(dls(G, start, end,1, set()), "Depth Limited Search Visualization - Depth 1", G, pos, end)

def on_depth2_button_click(event):
  visualize_search(dls(G, start, end,2,set()), "Depth Limited Search Visualization - Depth 2", G, pos, end)

def on_depth3_button_click(event):
  visualize_search(dls(G, start, end,3,set()), "Depth Limited Search Visualization - Depth 3", G, pos, end)

def on_depth4_button_click(event):
  visualize_search(dls(G, start, end,4,set()), "Depth Limited Search Visualization - Depth 4", G, pos, end)

def on_depth5_button_click(event):
  visualize_search(dls(G, start, end,5,set()), "Depth Limited Search Visualization - Depth 5", G, pos, end)

def on_depth6_button_click(event):
  visualize_search(dls(G, start, end,6,set()), "Depth Limited Search Visualization - Depth 6", G, pos, end)

def on_dls_button_click(event):
  fig, ax = plt.subplots()
  ax.clear()
  plt.clf()
  ax.set_title("Select Depth Limit")
  d1_button = Button(plt.axes([0.25, 0.75, 0.5, 0.075]), 'Depth 1', color=btn_color, hovercolor=btn_hover_color)
  d2_button = Button(plt.axes([0.25, 0.655, 0.5, 0.075]), 'Depth 2', color=btn_color, hovercolor=btn_hover_color)
  d3_button = Button(plt.axes([0.25, 0.56, 0.5, 0.075]), 'Depth 3', color=btn_color, hovercolor=btn_hover_color)
  d4_button = Button(plt.axes([0.25, 0.465, 0.5, 0.075]), 'Depth 4', color=btn_color, hovercolor=btn_hover_color)
  d5_button = Button(plt.axes([0.25, 0.37, 0.5, 0.075]), 'Depth 5', color=btn_color, hovercolor=btn_hover_color)
  d6_button = Button(plt.axes([0.25, 0.275, 0.5, 0.075]), 'Depth 6', color=btn_color, hovercolor=btn_hover_color)
  d1_button.on_clicked(on_depth1_button_click)
  d2_button.on_clicked(on_depth2_button_click)
  d3_button.on_clicked(on_depth3_button_click)
  d4_button.on_clicked(on_depth4_button_click)
  d5_button.on_clicked(on_depth5_button_click)
  d6_button.on_clicked(on_depth6_button_click)
  plt.show()

def on_idls_button_click(event):
  visualize_idls_search(start, end, "Iterative Deepening Search Visualization", G, pos)

def on_ucs_button_click(event):
  visualize_search(ucs(G, start, end), "Uniform Cost Search Visualization", G, pos, end)

def on_greedy_button_click(event):
  visualize_search(greedy(G, start, end), "Greedy Search Visualization", G, pos, end)

def on_a_star_button_click(event):
  visualize_search(a_star(G, start, end), "A Star Search Visualization", G, pos, end)


def main():
  plt.figure()
  plt.clf()
  bfs_button_ax = plt.axes([0.25, 0.75, 0.5, 0.075])
  dfs_button_ax = plt.axes([0.25, 0.655, 0.5, 0.075])
  dls_button_ax = plt.axes([0.25, 0.56, 0.5, 0.075])
  idls_button_ax = plt.axes([0.25, 0.465, 0.5, 0.075])
  ucs_button_ax = plt.axes([0.25, 0.37, 0.5, 0.075])
  greedy_button_ax = plt.axes([0.25, 0.275, 0.5, 0.075])
  a_star_button_ax = plt.axes([0.25, 0.18, 0.5, 0.075])
  bfs_button = Button(bfs_button_ax, 'Breadth First Search',color=btn_color, hovercolor=btn_hover_color)
  dfs_button = Button(dfs_button_ax, 'Depth First Search', color=btn_color, hovercolor=btn_hover_color)
  dls_button = Button(dls_button_ax, 'Depth Limited Search', color=btn_color, hovercolor=btn_hover_color)
  idls_button = Button(idls_button_ax, 'Iterative Deepening Search', color=btn_color, hovercolor=btn_hover_color)
  ucs_button = Button(ucs_button_ax, 'Uniform Cost Search', color=btn_color, hovercolor=btn_hover_color)
  greedy_button = Button(greedy_button_ax, 'Greedy Search', color=btn_color, hovercolor=btn_hover_color)
  a_star_button = Button(a_star_button_ax, 'A* Search', color=btn_color, hovercolor=btn_hover_color)
  bfs_button.on_clicked(on_bfs_button_click)
  dfs_button.on_clicked(on_dfs_button_click)
  dls_button.on_clicked(on_dls_button_click)
  idls_button.on_clicked(on_idls_button_click)
  ucs_button.on_clicked(on_ucs_button_click)
  greedy_button.on_clicked(on_greedy_button_click)
  a_star_button.on_clicked(on_a_star_button_click)
  plt.show()


main()
