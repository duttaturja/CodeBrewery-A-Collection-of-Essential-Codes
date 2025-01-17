class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

class PriorityScheduler:
    def __init__(self, processes):
        self.processes = processes

    def schedule(self):
        time = 0
        completed = 0
        n = len(self.processes)

        while completed < n:
            # Filter processes that have arrived and are not completed
            ready_queue = [p for p in self.processes if p.arrival_time <= time and p.remaining_time > 0]
            # Select the process with the highest priority (lowest priority value)
            if ready_queue:
                current_process = min(ready_queue, key=lambda x: x.priority)
                current_process.remaining_time -= 1
                time += 1
                if current_process.remaining_time == 0:
                    current_process.completion_time = time
                    current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                    current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                    completed += 1
            else:
                time += 1  # If no process is ready, advance time

    def display_results(self):
        print("PID\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting")
        for p in self.processes:
            print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.priority}\t\t{p.completion_time}\t\t{p.turnaround_time}\t\t{p.waiting_time}")

# Driver Code
if __name__ == "__main__":
    processes = [
        Process(1, 0, 8, 2),
        Process(2, 1, 4, 1),
        Process(3, 2, 9, 3),
        Process(4, 3, 5, 2)
    ]

    scheduler = PriorityScheduler(processes)
    scheduler.schedule()
    scheduler.display_results()
