from collections import defaultdict, deque


def bfs_shortest_paths(graph):
    shortest_paths = {}
    vertices = graph.keys()

    for source in vertices:
        distances = {v: float('inf') for v in vertices}
        predecessors = {v: None for v in vertices}
        distances[source] = 0

        queue = deque()
        queue.append(source)

        while queue:
            current = queue.popleft()

            for neighbor in graph[current]:
                if distances[neighbor] == float('inf'):
                    distances[neighbor] = distances[current] + 1
                    predecessors[neighbor] = current
                    queue.append(neighbor)

        shortest_paths[source] = (distances, predecessors)

    return shortest_paths


def get_shortest_path(predecessors, source, target):
    path = []
    current = target

    while current != source:
        path.append(current)
        current = predecessors[current]

        if current is None:
            return None

    path.append(source)
    path.reverse()
    return path


graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C', 'E'],
    'E': ['F'],
    'F': []
}

shortest_paths = bfs_shortest_paths(graph)

for source, (distances, predecessors) in shortest_paths.items():
    print(f"Shortest paths from vertex {source}:")
    for vertex in distances:
        print(
            f"To vertex {vertex}: Distance = {distances[vertex]}, Path = {get_shortest_path(predecessors, source, vertex)}")
    print()
