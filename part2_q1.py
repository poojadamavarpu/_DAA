import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def generate_random_numbers(n):
    return [random.randint(1, 10000) for _ in range(n)]

def compare_sorting_algorithms():
    sorting_algorithms = {
        'Bubble Sort': bubble_sort,
        'Merge Sort': merge_sort
    }
    time_taken = {}

    numbers = generate_random_numbers(1000)

    for name, sort_func in sorting_algorithms.items():
        arr = numbers.copy()
        start_time = time.time()
        sort_func(arr)
        end_time = time.time()
        time_taken[name] = end_time - start_time

    return time_taken

if __name__ == "__main__":
    time_taken = compare_sorting_algorithms()

    plt.bar(time_taken.keys(), time_taken.values())
    plt.ylabel('Time Taken (seconds)')
    plt.title('Sorting Algorithm Comparison')
    plt.show()
