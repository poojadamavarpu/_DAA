def inversion_count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

# Example usage:
arr = [10, 1, 2, 4, 13, 9, 5]
print(inversion_count(arr))
