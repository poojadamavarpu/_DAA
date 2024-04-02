def find_pair_sum_n2(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                return arr[i], arr[j]
    return None

# Example usage:
arr = [8, 4, 1, 6]
k = 10
print(find_pair_sum_n2(arr, k))
