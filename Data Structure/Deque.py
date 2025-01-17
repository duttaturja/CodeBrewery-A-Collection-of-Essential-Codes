from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def append(self, item):
        self.deque.append(item)

    def append_left(self, item):
        self.deque.appendleft(item)

    def pop(self):
        if not self.is_empty():
            return self.deque.pop()

    def pop_left(self):
        if not self.is_empty():
            return self.deque.popleft()

    def is_empty(self):
        return len(self.deque) == 0

# Example Usage
dq = Deque()
dq.append(10)
dq.append_left(20)
print(dq.pop())  # Output: 10
