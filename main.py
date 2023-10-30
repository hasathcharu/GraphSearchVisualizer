import queue
import networkx as nx
import matplotlib.pyplot as plt
from graph import G
from matplotlib.widgets import Button
from bfs import bfs
from dfs import dfs
from dls import dls
from ucs import ucs
from bidirectional import bidirectional
from greedy import greedy
from a_star import a_star
from utilities import get_node_color
from utilities import draw_graph
from utilities import get_text
from utilities import interleave_arrays
from utilities import draw_copyright_text
from backtrack import backtrack_path

start = "Haritha"
end = "Rashmi"
legend_colors = {
    "Not Visited": "#6ec2f7",
    "Currently Visiting / Path": "#fffaa0",
    "Visited": "#a686fc",
    "Start Node": "#ff7276",
    "Goal Node": "#7adc7a",
}
btn_color = "#9bfdcc"
btn_hover_color = "#63e0a2"
legend_elements = [
    plt.Line2D(
        [0],
        [0],
        marker="o",
        color="#111111",
        markerfacecolor=color,
        label=label,
        markersize=20,
    )
    for label, color in legend_colors.items()
]
edge_labels = nx.get_edge_attributes(G, "weight")
pos = {node: (x, y) for node, (x, y) in nx.get_node_attributes(G, "pos").items()}
figures = []
delay = 0.5


def visualize_search(order, title, G, position, end_node):
    path = backtrack_path(order[0], end_node, order, G)
    print("Traversal", order)
    print("Path", path)
    figure, ax = plt.subplots()
    ax.set_facecolor("#111111")
    draw_graph(
        title,
        get_text(order, path),
        position,
        edge_labels,
        legend_elements,
        G,
        [],
        order,
        end_node,
    )
    plt.pause(delay)
    for i, node in enumerate(order, start=1):
        draw_graph(
            title,
            get_text(order, path),
            position,
            edge_labels,
            legend_elements,
            G,
            [node],
            order,
            end_node,
        )
        plt.pause(delay)

    node = None
    figure.clear()
    draw_graph(
        title,
        get_text(order, path),
        position,
        edge_labels,
        legend_elements,
        G,
        [],
        order,
        end_node,
        True,
        path,
    )
    shortest_path = nx.shortest_path(
        G, source="Haritha", target="Rashmi", weight="weight"
    )
    print(shortest_path)
    plt.show()


def visualize_ucs_search(data, title, G, position, end_node):
    path = data[0]
    order = data[1]
    print("Traversal", order)
    print("Path", path)
    figure, ax = plt.subplots()
    ax.set_facecolor("#111111")
    draw_graph(
        title,
        get_text(order, path),
        position,
        edge_labels,
        legend_elements,
        G,
        [],
        order,
        end_node,
    )
    plt.pause(delay)
    for i, node in enumerate(order, start=1):
        draw_graph(
            title,
            get_text(order, path),
            position,
            edge_labels,
            legend_elements,
            G,
            [node],
            order,
            end_node,
        )
        plt.pause(delay)

    node = None
    figure.clear()
    draw_graph(
        title,
        get_text(order, path),
        position,
        edge_labels,
        legend_elements,
        G,
        [],
        order,
        end_node,
        True,
        path,
    )
    shortest_path = nx.shortest_path(
        G, source="Haritha", target="Rashmi", weight="weight"
    )
    print(shortest_path)
    plt.show()


def visualize_bidirectional_search(sorder, eorder, order, end_node, title, G, position):
    raw_order = sorder.copy()
    raw_order.extend(eorder)
    traverse_order = interleave_arrays(sorder, eorder)
    path = backtrack_path(order[0], end_node, order, G)
    print("Traversal", traverse_order)
    print("Path", path)
    figure, ax = plt.subplots()
    ax.set_facecolor("#111111")
    draw_graph(
        title,
        get_text(order, path),
        position,
        edge_labels,
        legend_elements,
        G,
        [],
        order,
        end_node,
    )
    i = 0
    plt.pause(delay)
    start_queue = sorder.copy()
    end_queue = eorder.copy()
    while len(start_queue) != 0 or len(end_queue) != 0:
        snode = ""
        enode = ""
        if len(start_queue) != 0:
            snode = start_queue[0]
            start_queue = start_queue[1:]
        if len(end_queue) != 0:
            enode = end_queue[0]
            end_queue = end_queue[1:]
        draw_graph(
            title,
            get_text(traverse_order, path),
            position,
            edge_labels,
            legend_elements,
            G,
            [snode, enode],
            order,
            end_node,
        )
        plt.pause(delay)
    figure.clear()
    draw_graph(
        title,
        get_text(traverse_order, path),
        position,
        edge_labels,
        legend_elements,
        G,
        [],
        raw_order,
        end_node,
        True,
        path,
    )
    plt.show()


def visualize_idls_search(start_node, end_node, title, G, position):
    figure, ax = plt.subplots()
    path = None
    figure.clear()
    order = []
    all_order = []
    for j in range(1, 10):
        order = dls(G, start_node, end_node, limit=j, visited=set())
        all_order.extend(order)
        path = backtrack_path(order[0], end_node, order, G)
        draw_graph(
            title + "\n\nDepth " + str(j),
            get_text(order, path),
            position,
            edge_labels,
            legend_elements,
            G,
            [],
            order,
            end_node,
        )
        plt.pause(delay)
        for i, node in enumerate(order, start=1):
            draw_graph(
                title + "\n\nDepth " + str(j),
                get_text(order, path),
                position,
                edge_labels,
                legend_elements,
                G,
                [node],
                order,
                end_node,
            )
            plt.pause(delay)
        if end_node in order:
            break
    node = None
    draw_graph(
        title + "\n\nDepth " + str(j),
        get_text(all_order, path),
        position,
        edge_labels,
        legend_elements,
        G,
        [],
        all_order,
        end_node,
        True,
        path,
    )
    plt.show()


def on_bfs_button_click(event):
    visualize_search(
        bfs(G, start, end), "Breadth First Search Visualization", G, pos, end
    )


def on_dfs_button_click(event):
    visualize_search(
        dfs(G, start, end), "Depth First Search Visualization", G, pos, end
    )


def on_depth1_button_click(event):
    visualize_search(
        dls(G, start, end, 1, set()),
        "Depth Limited Search Visualization - Depth 1",
        G,
        pos,
        end,
    )


def on_depth2_button_click(event):
    visualize_search(
        dls(G, start, end, 2, set()),
        "Depth Limited Search Visualization - Depth 2",
        G,
        pos,
        end,
    )


def on_depth3_button_click(event):
    visualize_search(
        dls(G, start, end, 3, set()),
        "Depth Limited Search Visualization - Depth 3",
        G,
        pos,
        end,
    )


def on_depth4_button_click(event):
    visualize_search(
        dls(G, start, end, 4, set()),
        "Depth Limited Search Visualization - Depth 4",
        G,
        pos,
        end,
    )


def on_depth5_button_click(event):
    visualize_search(
        dls(G, start, end, 5, set()),
        "Depth Limited Search Visualization - Depth 5",
        G,
        pos,
        end,
    )


def on_depth6_button_click(event):
    visualize_search(
        dls(G, start, end, 6, set()),
        "Depth Limited Search Visualization - Depth 6",
        G,
        pos,
        end,
    )


def on_dls_button_click(event):
    fig, ax = plt.subplots()
    fig.set_facecolor("#111111")
    ax.clear()
    plt.clf()
    plt.suptitle("Select Depth Limit", color="#eeeeee")
    d1_button = Button(
        plt.axes([0.25, 0.75, 0.5, 0.075]),
        "Depth 1",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    d2_button = Button(
        plt.axes([0.25, 0.655, 0.5, 0.075]),
        "Depth 2",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    d3_button = Button(
        plt.axes([0.25, 0.56, 0.5, 0.075]),
        "Depth 3",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    d4_button = Button(
        plt.axes([0.25, 0.465, 0.5, 0.075]),
        "Depth 4",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    d5_button = Button(
        plt.axes([0.25, 0.37, 0.5, 0.075]),
        "Depth 5",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    d6_button = Button(
        plt.axes([0.25, 0.275, 0.5, 0.075]),
        "Depth 6",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    d1_button.on_clicked(on_depth1_button_click)
    d2_button.on_clicked(on_depth2_button_click)
    d3_button.on_clicked(on_depth3_button_click)
    d4_button.on_clicked(on_depth4_button_click)
    d5_button.on_clicked(on_depth5_button_click)
    d6_button.on_clicked(on_depth6_button_click)
    draw_copyright_text()
    plt.show()


def on_idls_button_click(event):
    visualize_idls_search(
        start, end, "Iterative Deepening Search Visualization", G, pos
    )


def on_ucs_button_click(event):
    visualize_ucs_search(
        ucs(G, start, end), "Uniform Cost Search Visualization", G, pos, end
    )


def on_bidirectional_button_click(event):
    visualize_bidirectional_search(
        *bidirectional(G, start, end), end, "Bidirectional Search Visualization", G, pos
    )


def on_greedy_button_click(event):
    visualize_search(greedy(G, start, end), "Greedy Search Visualization", G, pos, end)


def on_a_star_button_click(event):
    visualize_search(a_star(G, start, end), "A Star Search Visualization", G, pos, end)


def main():
    fig, ax = plt.subplots()
    plt.clf()
    fig.set_facecolor("#111111")
    plt.suptitle("Graph Search Visualizer", color="#eeeeee")
    bfs_button_ax = plt.axes([0.25, 0.75, 0.5, 0.075])
    dfs_button_ax = plt.axes([0.25, 0.655, 0.5, 0.075])
    dls_button_ax = plt.axes([0.25, 0.56, 0.5, 0.075])
    idls_button_ax = plt.axes([0.25, 0.465, 0.5, 0.075])
    ucs_button_ax = plt.axes([0.25, 0.37, 0.5, 0.075])
    bidirectional_button_ax = plt.axes([0.25, 0.275, 0.5, 0.075])
    greedy_button_ax = plt.axes([0.25, 0.18, 0.5, 0.075])
    a_star_button_ax = plt.axes([0.25, 0.085, 0.5, 0.075])
    bfs_button = Button(
        bfs_button_ax,
        "Breadth First Search",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    dfs_button = Button(
        dfs_button_ax, "Depth First Search", color=btn_color, hovercolor=btn_hover_color
    )
    dls_button = Button(
        dls_button_ax,
        "Depth Limited Search",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    idls_button = Button(
        idls_button_ax,
        "Iterative Deepening Search",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    ucs_button = Button(
        ucs_button_ax,
        "Uniform Cost Search",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    bidirectional_button = Button(
        bidirectional_button_ax,
        "Bidirectional Search",
        color=btn_color,
        hovercolor=btn_hover_color,
    )
    greedy_button = Button(
        greedy_button_ax, "Greedy Search", color=btn_color, hovercolor=btn_hover_color
    )
    a_star_button = Button(
        a_star_button_ax, "A* Search", color=btn_color, hovercolor=btn_hover_color
    )
    bfs_button.on_clicked(on_bfs_button_click)
    dfs_button.on_clicked(on_dfs_button_click)
    dls_button.on_clicked(on_dls_button_click)
    idls_button.on_clicked(on_idls_button_click)
    ucs_button.on_clicked(on_ucs_button_click)
    bidirectional_button.on_clicked(on_bidirectional_button_click)
    greedy_button.on_clicked(on_greedy_button_click)
    a_star_button.on_clicked(on_a_star_button_click)
    draw_copyright_text()
    plt.show()


# print(bidirectional(G, start, end))
main()
