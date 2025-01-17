import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]

    def peek(self):
        if not self.is_empty():
            return self.queue[0][1]

    def is_empty(self):
        return len(self.queue) == 0

# Example Usage
pq = PriorityQueue()
pq.push("Task1", 2)
pq.push("Task2", 1)
print(pq.pop())  # Output: Task2
