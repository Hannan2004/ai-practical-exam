def depth_limited_dfs(graph, current, goal, limit, path, visited, depth=0):
    """
    Helper function to perform Depth-Limited DFS.

    :param graph: Adjacency list of the graph.
    :param current: Current node.
    :param goal: Goal node.
    :param limit: Current depth limit.
    :param path: Current path.
    :param visited: Set of visited nodes at this depth.
    :param depth: Current depth level.
    :return: Path to goal if found, else None.
    """
    print(f"Visiting: {current} | Depth: {depth} | Path: {path}")
    
    if current == goal:
        return path
    if depth >= limit:
        return None

    visited.add(current)
    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            result = depth_limited_dfs(graph, neighbor, goal, limit, path + [neighbor], visited.copy(), depth + 1)
            if result:
                return result
    return None

def iterative_deepening_dfs(graph, start, goal, max_depth=50):
    """
    Performs IDDFS from start to goal node, printing traversal steps.

    :param graph: Adjacency list of the graph.
    :param start: Starting node.
    :param goal: Goal node.
    :param max_depth: Maximum depth to limit IDDFS search.
    :return: Final path to goal if found, else None.
    """
    print("\nStarting Iterative Deepening DFS...")
    for depth in range(max_depth):
        print(f"\n--- Depth Limit: {depth} ---")
        visited = set()
        path = depth_limited_dfs(graph, start, goal, depth, [start], visited)
        if path:
            print("\nGoal reached!")
            print("Final path:", path)
            return path
    print("\nNo path found within depth limit.")
    return None

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("\nTest Case: From A to F")
    iterative_deepening_dfs(graph, 'A', 'F')

    print("\nTest Case: From A to A")
    iterative_deepening_dfs(graph, 'A', 'A')

    print("\nTest Case: From A to Z (unreachable)")
    graph_unreachable = {
        'A': ['B'],
        'B': ['C'],
        'C': [],
        'Z': []
    }
    iterative_deepening_dfs(graph_unreachable, 'A', 'Z', max_depth=10)
