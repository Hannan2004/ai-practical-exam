import random

def calculate_total_distance(path, distance_matrix):
    """Calculate the total distance of the path based on distance matrix."""
    total = 0
    for i in range(len(path)):
        total += distance_matrix[path[i]][path[(i + 1) % len(path)]]  # loop back to start
    return total

def get_neighbors(path):
    """Generate neighbors by swapping two cities."""
    neighbors = []
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            neighbor = path.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(distance_matrix, cities):
    """Solve TSP using Hill Climbing."""
    # Start with a random path
    current_path = cities.copy()
    random.shuffle(current_path)
    current_cost = calculate_total_distance(current_path, distance_matrix)

    print(f"Initial path: {current_path}, Cost: {current_cost}")

    while True:
        neighbors = get_neighbors(current_path)
        neighbor_costs = [(calculate_total_distance(neighbor, distance_matrix), neighbor) for neighbor in neighbors]

        # Pick the best neighbor
        best_neighbor_cost, best_neighbor = min(neighbor_costs, key=lambda x: x[0])

        if best_neighbor_cost < current_cost:
            print(f"Moving to better neighbor: {best_neighbor}, Cost: {best_neighbor_cost}")
            current_path, current_cost = best_neighbor, best_neighbor_cost
        else:
            # No better neighbor found
            print(f"No better neighbor found. Final path: {current_path}, Cost: {current_cost}")
            break

    return current_path, current_cost

# Example usage
if __name__ == "__main__":
    # Distance matrix (symmetric)
    distance_matrix = [
        [0, 10, 15, 20],  # City 0
        [10, 0, 35, 25],  # City 1
        [15, 35, 0, 30],  # City 2
        [20, 25, 30, 0]   # City 3
    ]
    
    cities = [0, 1, 2, 3]

    final_path, final_cost = hill_climbing(distance_matrix, cities)
    print(f"\nBest path found: {final_path} with total cost: {final_cost}")
