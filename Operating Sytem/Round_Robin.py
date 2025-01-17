class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

class RoundRobinScheduler:
    def __init__(self, processes, time_quantum):
        self.processes = processes
        self.time_quantum = time_quantum

    def schedule(self):
        self.processes.sort(key=lambda p: p.arrival_time)  # Sort by arrival time
        time = 0
        queue = []
        completed = 0
        n = len(self.processes)

        while completed < n:
            for process in self.processes:
                if process.arrival_time <= time and process not in queue and process.remaining_time > 0:
                    queue.append(process)

            if queue:
                current_process = queue.pop(0)
                if current_process.remaining_time > self.time_quantum:
                    time += self.time_quantum
                    current_process.remaining_time -= self.time_quantum
                else:
                    time += current_process.remaining_time
                    current_process.remaining_time = 0
                    current_process.completion_time = time
                    current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                    current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                    completed += 1

                for process in self.processes:
                    if process.arrival_time <= time and process not in queue and process.remaining_time > 0:
                        queue.append(process)

                if current_process.remaining_time > 0:
                    queue.append(current_process)
            else:
                time += 1

    def print_results(self):
        print("PID\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
        for process in self.processes:
            print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

# Driver Code
def main():
    n = int(input("Enter the number of processes: "))
    processes = []

    for i in range(n):
        pid = i + 1
        arrival_time = int(input(f"Enter arrival time for process {pid}: "))
        burst_time = int(input(f"Enter burst time for process {pid}: "))
        processes.append(Process(pid, arrival_time, burst_time))

    time_quantum = int(input("Enter time quantum: "))
    scheduler = RoundRobinScheduler(processes, time_quantum)
    scheduler.schedule()
    scheduler.print_results()

if __name__ == "__main__":
    main()
