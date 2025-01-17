def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example Usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = linear_search(arr, target)
print(f"Linear Search: Target {target} found at index {result}" if result != -1 else "Not Found")
