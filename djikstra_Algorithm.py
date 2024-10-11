import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity and set start node distance to 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue to store (distance, vertex)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded distance, skip
        if current_distance > distances[current_vertex]:
            continue

        # Examine neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If the distance to a neighbor is less, update the shortest distance and push to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph representation
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"Shortest paths from {start_node}: {shortest_paths}")
