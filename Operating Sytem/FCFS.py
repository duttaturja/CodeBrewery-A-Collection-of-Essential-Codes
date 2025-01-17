class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

class FCFSScheduler:
    def __init__(self, processes):
        self.processes = processes

    def schedule(self):
        self.processes.sort(key=lambda p: p.arrival_time)  # Sort by arrival time
        current_time = 0

        for process in self.processes:
            if current_time < process.arrival_time:
                current_time = process.arrival_time

            process.completion_time = current_time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            current_time += process.burst_time

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

    scheduler = FCFSScheduler(processes)
    scheduler.schedule()
    scheduler.print_results()

if __name__ == "__main__":
    main()