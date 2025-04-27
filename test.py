def minimax(node, depth, maximizingPlayer, graph):
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
    
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': 3,
    'I': 5,
    'J': 6,
    'K': 9,
    'L': 1,
    'M': 2,
    'N': 0,
    'O': -1
}

best_value = minimax('A', depth=3, maximizingPlayer=True, graph=graph)
print(f"\nBest value achievable from root: {best_value}")