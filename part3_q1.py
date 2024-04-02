def find_pair_with_sum(arr, target_sum):
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return complement, num
        seen.add(num)
    return None

# Example usage:
arr = [1, 7, 4, 2, 8, 6, 3, 9, 5]
target_sum = 17
print(find_pair_with_sum(arr, target_sum))
