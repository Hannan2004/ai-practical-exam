def minimax(node, depth, maximizingPlayer, graph):
    """
    Minimax algorithm implementation.

    Args:
    - node: current node id (index or name)
    - depth: how deep we are in the tree
    - maximizingPlayer: True if it's maximizer's move, False for minimizer
    - graph: dict with nodes mapping to either a list of children or a terminal value

    Returns:
    - Best score achievable from this node
    """

    # If we reach a terminal node (leaf) or max depth
    if isinstance(graph[node], int) or depth == 0:
        print(f"Reached leaf {node} with value {graph[node]}")
        return graph[node]

    if maximizingPlayer:
        maxEval = float('-inf')
        print(f"Maximizing at node {node}")
        for child in graph[node]:
            eval = minimax(child, depth-1, False, graph)
            maxEval = max(maxEval, eval)
        print(f"Best for maximizer at node {node}: {maxEval}")
        return maxEval
    else:
        minEval = float('inf')
        print(f"Minimizing at node {node}")
        for child in graph[node]:
            eval = minimax(child, depth-1, True, graph)
            minEval = min(minEval, eval)
        print(f"Best for minimizer at node {node}: {minEval}")
        return minEval

# Example usage

if __name__ == "__main__":
    # Simple example tree:
    # Graph structure:
    #         A
    #      /  |  \
    #    B    C   D
    #   / \   |   / \
    #  3  5  2  9  12

    graph = {
        'A': ['B', 'C', 'D'],
        'B': [3, 5],
        'C': [2],
        'D': [9, 12]
    }

    best_value = minimax('A', depth=3, maximizingPlayer=True, graph=graph)
    print(f"\nBest value achievable from root: {best_value}")
