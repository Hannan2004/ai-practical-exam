import heapq

def ucs(graph, start, goal):
    queue = [(0, start, [start])]
    heapq.heapify(queue)
    
    visited = {}
    
    while queue: 
        cost, node, path = heapq.heappop(queue)
        
        print(f"Current Node: {node} | Cost: {cost} | Path: {path}")
        
        if node == goal:
            return cost, path
            
        if node in visited and visited[node] <= cost:
            continue
        
        visited[node] = cost
        
        for neighbor, edge_cost in graph.get(node,[]):
            total_cost = cost + edge_cost
            heapq.heappush(queue, (total_cost , neighbor, path + [neighbor]))
    return float('inf'), []
    
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    
    cost, path = ucs(graph, 'A', 'C')
    print(f"Cost: {cost}, Path: {path}")     