def sort_swapped_array(arr):
    n = len(arr)
    x = y = -1

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if x == -1:
                x = i
            else:
                y = i + 1
                break

    arr[x], arr[y] = arr[y], arr[x]

# Example usage:
arr = [1, 5, 3, 4, 2, 6]
sort_swapped_array(arr)
print(arr)
