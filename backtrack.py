def backtrack_path(start_node, end_node, order, graph):
    if end_node not in order:
        return []
    path = []
    path.append(end_node)
    for i in range(len(order) - 1, 0, -1):
        if order[i] in graph.neighbors(path[-1]):
            path.append(order[i])
    path.append(start_node)
    return path[::-1]
