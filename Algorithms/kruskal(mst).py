import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim(self, start):
        min_heap = [(0, start)]
        visited = set()
        mst = []
        total_weight = 0

        while min_heap:
            weight, vertex = heapq.heappop(min_heap)

            if vertex not in visited:
                visited.add(vertex)
                mst.append((vertex, weight))
                total_weight += weight

                for neighbor, edge_weight in self.graph[vertex]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (edge_weight, neighbor))

        return mst, total_weight

# Example Usage
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst, total_weight = g.prim(0)
print("Minimum Spanning Tree:", mst)
print("Total Weight:", total_weight)
