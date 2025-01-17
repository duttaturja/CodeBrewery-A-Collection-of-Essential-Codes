
import heapq

def a_star_search(graph, heuristic, start, goal):
    priority_queue = [(0 + heuristic[start], 0, start, [])]
    visited = set()

    while priority_queue:
        _, cost, node, path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == goal:
            return path, cost
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight + heuristic[neighbor], cost + weight, neighbor, path))
    return None

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('D', 1), ('E', 4)],
        'C': [('F', 2)],
        'D': [],
        'E': [('F', 1)],
        'F': []
    }
    heuristic = {
        'A': 5,
        'B': 3,
        'C': 4,
        'D': 3,
        'E': 1,
        'F': 0
    }
    print(a_star_search(graph, heuristic, 'A', 'F'))
