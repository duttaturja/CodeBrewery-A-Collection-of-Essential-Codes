def ternary_search(arr, target, left, right):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            return ternary_search(arr, target, left, mid1 - 1)
        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2 + 1, right)
        else:
            return ternary_search(arr, target, mid1 + 1, mid2 - 1)
    return -1

# Example Usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = ternary_search(arr, target, 0, len(arr)-1)
print(f"Ternary Search: Target {target} found at index {result}" if result != -1 else "Not Found")
