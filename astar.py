import heapq

def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = {}

    while open_set:
        f_score, g_score, current, path = heapq.heappop(open_set)
        print(f"Visiting: {current} | Path: {path} | Cost: {g_score}")
        if current == goal:
            return path, g_score
        
        if current in visited and visited[current] <= g_score:
            continue

        visited[current] = g_score

        for neighbor, cost in graph.get(current, []):
            tentative_g_score = g_score + cost
            tentative_f_score = tentative_g_score + heuristic(neighbor, goal)
            heapq.heappush(open_set, (tentative_f_score, tentative_g_score, neighbor, path + [neighbor]))

    return None, float('inf')

if __name__ == "__main__":
    graph = {
        'S': [('A', 1), ('G', 10)],
        'A': [('B', 2), ('C', 1)],
        'B': [('D', 5)],
        'C': [('D', 3), ('G', 4)],
        'D': [('G', 2)],
        'G': []
    }

    heuristic_values = {
        'S': 5,
        'A': 3,
        'B': 4,
        'C': 2,
        'D': 6,
        'G': 0
    }

    def heuristic(u, v):
        return heuristic_values[u]
    
    path, cost = a_star(graph, 'S', 'G', heuristic)

    print(f"Path: {path} | Cost: {cost}")