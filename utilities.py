import matplotlib.pyplot as plt
import networkx as nx


def interleave_arrays(arr1, arr2):
    # Determine the length of the output array
    length = min(len(arr1), len(arr2))

    # Interlock the arrays using list comprehension
    interlocked = [val for pair in zip(arr1[:length], arr2[:length]) for val in pair]

    # If one array is longer than the other, append the remaining elements
    if len(arr1) > len(arr2):
        interlocked.extend(arr1[length:])
    elif len(arr2) > len(arr1):
        interlocked.extend(arr2[length:])

    return interlocked


def get_node_color(node, order, end_node, graph, final=False, path=[]):
    color_map = []
    if len(order) == 0:
        return "b"
    for i in graph.nodes:
        color = "#6ec2f7"
        if i in order and final:
            color = "#a686fc"
        if i in path:
            color = "#fffaa0"
        if i == end_node:
            color = "#9bfdcc"
        if i == order[0]:
            color = "#ff7276"
        if i in node:
            color = "#fffaa0"
        color_map.append(color)
    return color_map


def draw_copyright_text(G=None):
    x = 0.5
    y = -1
    if G:
        positions = [
            (x, y) for node, (x, y) in nx.get_node_attributes(G, "pos").items()
        ]
        x = sum([x for (x, y) in positions]) / len(positions)
        y = min([y for (x, y) in positions]) - 1.3
    plt.text(x, y, "Made with ❤️ by Haritha Hasathcharu", color="#eeeeee", ha="center")


def draw_graph(
    title,
    text_content,
    position,
    edge_labels,
    legend_elements,
    G,
    node,
    order,
    end_node,
    final=False,
    path=[],
):
    plt.gcf().clf()
    plt.suptitle(title, color="#eeeeee")
    plt.text(2.5, -4, text_content, color="#eeeeee")
    nx.draw(
        G,
        position,
        with_labels=True,
        node_color=get_node_color(node, order, end_node, G, final, path),
        node_size=5000,
        edge_color="#eeeeee",
    )
    nx.draw_networkx_labels(
        G,
        {
            node: (x, y - 0.2)
            for node, (x, y) in nx.get_node_attributes(G, "pos").items()
        },
        labels={
            node: "h=" + str(h) for node, h in nx.get_node_attributes(G, "h").items()
        },
        font_color="#333333",
    )
    nx.draw_networkx_edge_labels(
        G, position, edge_labels=edge_labels, font_color="#333333"
    )
    legend = plt.legend(
        handles=legend_elements, loc="lower right", handletextpad=1, labelspacing=1.5
    )
    legend.get_frame().set_facecolor("#111111")
    legend.get_frame().set_linewidth(0)
    legend.get_frame().set_edgecolor("none")
    for text in legend.get_texts():
        text.set_color("#eeeeee")
    draw_copyright_text(G)
    plt.gcf().set_facecolor("#111111")
    plt.gca().set_facecolor("#111111")
    plt.draw()


def get_text(order, path):
    path_text = (", ").join(path[i] for i in range(len(path)))
    if len(path_text) == 0:
        path_text = "No path found"

    return "Traversal: " + (", ").join(order) + "\nPath: " + path_text
