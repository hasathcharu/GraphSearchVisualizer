def ucs(graph, start, goal):
    visited = []
    entry_counter = 0
    queue = [(0, entry_counter, start, [])]
    while queue:
        print(queue)

        cost, entry, node, path = queue.pop(0)
        print((cost, entry, node, path))
        if node == goal:
            path.append(node)
            visited.append(node)
            return visited, path

        if node in visited:
            continue

        visited.append(node)

        for neighbor in graph.neighbors(node):
            weight = graph.get_edge_data(node, neighbor).get("weight", 0)
            if neighbor not in visited:
                new_cost = cost + weight
                new_path = path + [node]
                entry_counter += 1
                queue.append((new_cost, entry_counter, neighbor, new_path))

        queue.sort()

    return [], visited
