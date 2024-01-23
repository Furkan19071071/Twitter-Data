from MyQueue import Queue
def bfs(graph, start_node):
    queue = Queue()
    queue.enqueue(start_node)
    visited = set([start_node])
    common_neighbors = set()

    while not queue.is_empty():
        current_node = queue.dequeue()
        for neighbor in graph.nodes[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
                common_neighbors.add(neighbor)


    return common_neighbors
