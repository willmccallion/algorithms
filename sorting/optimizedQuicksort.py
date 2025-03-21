import random
import sys

def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    # Randomly select a pivot and swap with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low  # place for swapping
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def optimized_random_quicksort(arr, low, high):
    # Use insertion sort for small partitions to reduce overhead
    if high - low <= 10:
        insertion_sort(arr, low, high)
        return
    if low < high:
        pivot_index = partition(arr, low, high)
        optimized_random_quicksort(arr, low, pivot_index - 1)
        optimized_random_quicksort(arr, pivot_index + 1, high)

def sort(arr):
    optimized_random_quicksort(arr, 0, len(arr) - 1)
    return arr

# Generates an array of random numbers with a size of size.
def generate_large_array(size: int) -> list:
    return [random.randint(0, size) for _ in range(size)]

if __name__ == "__main__":
    size = int(sys.argv[1])
    A = generate_large_array(size)
    sort(A)
    if len(sys.argv) == 3:
        print(A)

