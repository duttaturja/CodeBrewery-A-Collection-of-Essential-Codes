import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Example Usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = jump_search(arr, target)
print(f"Jump Search: Target {target} found at index {result}" if result != -1 else "Not Found")
