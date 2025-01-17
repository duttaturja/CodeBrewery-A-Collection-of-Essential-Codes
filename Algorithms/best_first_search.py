
import heapq

def best_first_search(graph, start, goal):
    priority_queue = [(0, start)]
    visited = set()
    path = []

    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        if node == goal:
            return path
        for cost, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost, neighbor))
    return None

if __name__ == "__main__":
    graph = {
        'A': [(1, 'B'), (3, 'C')],
        'B': [(1, 'D'), (4, 'E')],
        'C': [(2, 'F')],
        'D': [],
        'E': [(1, 'F')],
        'F': []
    }
    print(best_first_search(graph, 'A', 'F'))
