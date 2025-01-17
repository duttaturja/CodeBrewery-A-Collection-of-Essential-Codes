class BankersAlgorithm:
    def __init__(self, allocation, maximum, available):
        self.allocation = allocation  # Allocated resources for each process
        self.maximum = maximum        # Maximum resources required by each process
        self.available = available    # Available resources
        self.num_processes = len(allocation)
        self.num_resources = len(available)
        self.need = self.calculate_need()

    def calculate_need(self):
        # Calculate the Need matrix as Maximum - Allocation
        need = []
        for i in range(self.num_processes):
            need.append([self.maximum[i][j] - self.allocation[i][j] for j in range(self.num_resources)])
        return need

    def is_safe_state(self):
        work = self.available[:]  # Copy of available resources
        finish = [False] * self.num_processes
        safe_sequence = []

        while len(safe_sequence) < self.num_processes:
            allocated = False
            for i in range(self.num_processes):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(self.num_resources)):
                    work = [work[j] + self.allocation[i][j] for j in range(self.num_resources)]
                    safe_sequence.append(i)
                    finish[i] = True
                    allocated = True
            if not allocated:
                break

        return finish, safe_sequence

    def detect_deadlock(self):
        finish, safe_sequence = self.is_safe_state()
        deadlocked_processes = [i for i in range(self.num_processes) if not finish[i]]
        if deadlocked_processes:
            return deadlocked_processes
        return safe_sequence

# Driver Code
if __name__ == "__main__":
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    maximum = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [4, 2, 2],
        [5, 3, 3]
    ]
    available = [3, 3, 2]

    banker = BankersAlgorithm(allocation, maximum, available)
    result = banker.detect_deadlock()

    if isinstance(result, list) and all(isinstance(i, int) for i in result):
        print("Deadlock detected! Processes involved:", result)
    else:
        print("No deadlock detected. Safe sequence:", [p + 1 for p in result])
