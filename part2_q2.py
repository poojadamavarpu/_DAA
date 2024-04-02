import heapq

def merge_sorted_lists(arrays):
    heap = []
    result = []

    for i, array in enumerate(arrays):
        if array:
            heapq.heappush(heap, (array[0], i, 0))

    while heap:
        val, array_idx, idx = heapq.heappop(heap)
        result.append(val)

        if idx + 1 < len(arrays[array_idx]):
            heapq.heappush(heap, (arrays[array_idx][idx + 1], array_idx, idx + 1))

    return result

# Example usage:
arrays = [[1, 3, 5], [2, 4, 6], [0, 7, 8]]
print(merge_sorted_lists(arrays))
