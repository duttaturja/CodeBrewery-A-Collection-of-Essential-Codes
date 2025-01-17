
import random

def calculate_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing(n=8):
    current = [random.randint(0, n - 1) for _ in range(n)]
    while True:
        neighbors = []
        current_conflicts = calculate_conflicts(current)
        for i in range(n):
            for j in range(n):
                if j != current[i]:
                    neighbor = current[:]
                    neighbor[i] = j
                    neighbors.append((calculate_conflicts(neighbor), neighbor))
        neighbors.sort(key=lambda x: x[0])
        if neighbors[0][0] >= current_conflicts:
            break
        current = neighbors[0][1]
    return current, calculate_conflicts(current)

if __name__ == "__main__":
    solution, conflicts = hill_climbing()
    print("Solution:", solution)
    print("Conflicts:", conflicts)
