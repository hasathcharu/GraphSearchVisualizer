from backtrack import backtrack_path


def dfs_recurs(graph, start_node, end_node, visited=set()):
    if visited is None:
        visited = set()
    order = []
    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                order.extend(dfs_recurs(graph, node, end_node, visited))
            if end_node in order:
                break
    return order


def dfs(graph, start_node, end_node):
    order = dfs_recurs(graph, start_node, end_node, set())
    return order, backtrack_path(start_node, end_node, order, graph)
