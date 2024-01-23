
from MyStack import Stack

def dfs(graph, start_node):
    stack = Stack()  # Change the name to 'stack' to match the class name
    stack.push(start_node)
    visited = set([start_node])
    common_neighbors = set()

    while not stack.is_empty():
        current_node = stack.pop()
        for neighbor in graph.nodes[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.push(neighbor)
                common_neighbors.add(neighbor)

    return common_neighbors
