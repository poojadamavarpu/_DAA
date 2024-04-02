def segregate_0s_1s(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1
        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1

# Example usage:
arr = [0, 1, 0, 1, 1, 0, 0, 1]
segregate_0s_1s(arr)
print(arr)
