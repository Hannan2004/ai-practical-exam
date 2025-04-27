from collections import deque

def breadth_first_search(graph, start, goal):
    """
    Performs Breadth-First Search (BFS) from start to goal node.

    :param graph: Dict representing adjacency list of the graph.
    :param start: Start node.
    :param goal: Goal node.
    :return: List representing the shortest path from start to goal or None.
    """
    queue = deque([(start, [start])])
    visited = set()

    print("Traversal steps:")
    while queue:
        current, path = queue.popleft()
        print(f"Visiting: {current} | Current path: {path}")
        if current == goal:
            print("\nGoal reached!")
            print("Final path:", path)
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    print("\nNo path found.")
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

    print("\nTest Case 1: A to F")
    breadth_first_search(graph, 'A', 'F')  # Should return shortest path: ['A', 'C', 'F']

    print("\nTest Case 2: A to A")
    breadth_first_search(graph, 'A', 'A')  # Should return: ['A']

    print("\nTest Case 3: A to Z (unreachable)")
    graph_disconnected = {
        'A': ['B'],
        'B': ['C'],
        'C': [],
        'Z': []
    }
    breadth_first_search(graph_disconnected, 'A', 'Z')  # Should return: None
