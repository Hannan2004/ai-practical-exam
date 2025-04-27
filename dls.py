def depth_limited_search(graph, current, goal, limit, path=None, visited=None, depth=0):
    """
    Performs Depth-Limited Search (DLS) from the current node to the goal node.

    :param graph: Dict representing adjacency list of the graph.
    :param current: Current node in traversal.
    :param goal: Goal node to find.
    :param limit: Maximum allowed depth.
    :param path: Current path (list of nodes).
    :param visited: Set of visited nodes.
    :param depth: Current depth level.
    :return: Path if found, else None.
    """
    if path is None:
        path = [current]
    if visited is None:
        visited = set()

    print(f"Visiting: {current} | Depth: {depth} | Path: {path}")

    if current == goal:
        return path
    if depth >= limit:
        return None

    visited.add(current)

    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            result = depth_limited_search(graph, neighbor, goal, limit, path + [neighbor], visited.copy(), depth + 1)
            if result:
                return result

    return None

def run_dls(graph, start, goal, depth_limit):
    print(f"\nRunning Depth-Limited Search from {start} to {goal} with limit = {depth_limit}\n")
    path = depth_limited_search(graph, start, goal, depth_limit)
    if path:
        print("\nGoal reached!")
        print("Final path:", path)
    else:
        print("\nGoal not found within the depth limit.")

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("\nTest Case 1: A to F with depth limit 2")
    run_dls(graph, 'A', 'F', depth_limit=2)  # May not reach F

    print("\nTest Case 2: A to F with depth limit 3")
    run_dls(graph, 'A', 'F', depth_limit=3)  # Should succeed

    print("\nTest Case 3: A to A with depth limit 0")
    run_dls(graph, 'A', 'A', depth_limit=0)  # Should succeed

    print("\nTest Case 4: A to Z (unreachable)")
    graph_unreachable = {
        'A': ['B'],
        'B': ['C'],
        'C': [],
        'Z': []
    }
    run_dls(graph_unreachable, 'A', 'Z', depth_limit=5)
