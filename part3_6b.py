def find_pair_sum_nlogn(arr, k):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == k:
            return arr[left], arr[right]
        elif current_sum < k:
            left += 1
        else:
            right -= 1
    return None

# Example usage:
arr = [8, 4, 1, 6]
k = 10
print(find_pair_sum_nlogn(arr, k))
