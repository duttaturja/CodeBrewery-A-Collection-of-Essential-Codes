def unsorted_linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example Usage
arr = [15, 2, 8, 3, 10, 7]
target = 10
result = unsorted_linear_search(arr, target)
print(f"Unsorted Linear Search: Target {target} found at index {result}" if result != -1 else "Not Found")
