class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

class SJFNonPreemptiveScheduler:
    def __init__(self, processes):
        self.processes = processes

    def schedule(self):
        time = 0
        completed = 0
        n = len(self.processes)
        self.processes.sort(key=lambda p: p.arrival_time)  # Sort by arrival time
        
        while completed < n:
            # Get the process with the shortest burst time that has arrived and is not completed
            current_process = None
            for process in self.processes:
                if process.arrival_time <= time and process.completion_time == 0:
                    if current_process is None or process.burst_time < current_process.burst_time:
                        current_process = process

            if current_process is None:
                time += 1
                continue

            # Execute the selected process
            time += current_process.burst_time
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed += 1

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

    scheduler = SJFNonPreemptiveScheduler(processes)
    scheduler.schedule()
    scheduler.print_results()

if __name__ == "__main__":
    main()
