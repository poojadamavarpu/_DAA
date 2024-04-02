import heapq

def find_k_largest(arr, k):
    return heapq.nlargest(k, arr)

# Example usage:
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
k = 3
print(find_k_largest(arr, k))
