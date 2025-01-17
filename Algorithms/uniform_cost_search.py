
import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]
    visited = set()
    costs = {start: 0}

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return cost
        for next_cost, neighbor in graph[node]:
            total_cost = cost + next_cost
            if neighbor not in costs or total_cost < costs[neighbor]:
                costs[neighbor] = total_cost
                heapq.heappush(priority_queue, (total_cost, neighbor))
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
    print(uniform_cost_search(graph, 'A', 'F'))
