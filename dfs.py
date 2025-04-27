def depth_first_search(graph, start, goal):
    """
    Performs DFS on a graph from start node to goal node,
    showing the traversal path at each step.

    :param graph: Dict representing adjacency list of the graph.
    :param start: Starting node.
    :param goal: Goal node to search for.
    :return: Final path from start to goal, or None if no path exists.
    """
    stack = [(start, [start])]
    visited = set()

    print("Traversal steps:")
    while stack:
        (current, path) = stack.pop()
        print(f"Visiting: {current} | Current path: {path}")
        if current == goal:
            print("\nGoal reached!")
            print("Final path:", path)
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    print("\nNo path found.")
    return None

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': []
    }

    print("\nTest Case 1: From A to F")
    depth_first_search(graph, 'A', 'F')

    print("\nTest Case 2: From A to A")
    depth_first_search(graph, 'A', 'A')

    print("\nTest Case 3: From A to Z (unreachable)")
    graph_with_unreachable = {
        'A': ['B'],
        'B': ['C'],
        'C': [],
        'Z': []
    }
    depth_first_search(graph_with_unreachable, 'A', 'Z')
