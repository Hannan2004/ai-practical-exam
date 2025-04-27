import heapq

def greedy_best_first_search(graph, heuristics, start, goal):
    """
    Perform Greedy Best-First Search (GBFS) on a graph.

    Args:
    - graph: Dict where keys are node names and values are lists of (neighbor, cost) pairs.
    - heuristics: Dict mapping node to its heuristic value (estimated cost to goal).
    - start: The starting node.
    - goal: The goal node.

    Returns:
    - (path): The path taken to reach the goal.
    """

    # Priority queue: (heuristic value, node, path)
    queue = [(heuristics[start], start, [start])]
    heapq.heapify(queue)

    # Visited set
    visited = set()

    while queue:
        h_value, node, path = heapq.heappop(queue)
        print(f"Visiting node: {node}, Heuristic: {h_value}")

        if node == goal:
            print(f"Goal {goal} found! Path: {path}\n")
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristics.get(neighbor, float('inf')), neighbor, path + [neighbor]))

    # Goal not reachable
    print(f"Goal {goal} not reachable from {start}\n")
    return []

# Example Usage

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    
    heuristics = {
        'A': 5,
        'B': 3,
        'C': 2,
        'D': 0
    }
    
    path = greedy_best_first_search(graph, heuristics, 'A', 'D')
    print(f"Final Path: {path}")
