# def ucs(graph, start_node, end_node):
#     visited = set()
#     q = queue.PriorityQueue()
#     entry_counter = 0
#     q.put((0, entry_counter, start_node))
#     order = []
#     while not q.empty():
#         vertex = q.get()
#         if vertex not in visited:
#             visited.add(vertex[2])
#             order.append(vertex[2])
#             for node in graph[vertex[2]]:
#                 if node not in visited and all(node != item[2] for item in q.queue):
#                     entry_counter += 1
#                     q.put(
#                         (
#                             graph[vertex[2]][node]["weight"] + vertex[0],
#                             entry_counter,
#                             node,
#                         )
#                     )
#         if vertex[2] == end_node:
#             break

#     return order


def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]

    while queue:
        cost, node, path = queue.pop(0)

        if node == goal:
            path.append(node)
            return path, list(visited)

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph.neighbors(node):
            weight = graph.get_edge_data(node, neighbor).get("weight", 0)
            if neighbor not in visited:
                new_cost = cost + weight
                new_path = path + [node]
                queue.append((new_cost, neighbor, new_path))

        queue.sort()

    return [], list(visited)
