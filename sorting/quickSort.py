import random
import sys

# Implementation of quicksort algorithm. Runtime: O(nlogn)
def quicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    # Select pivot value as the last element
    pivot = arr[len(arr)-1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right partitions, then combine
    return quicksort(left) + middle + quicksort(right)

# Generates an array of random numbers with a size of size.
def generate_large_array(size: int) -> list:
    return [random.randint(0, size) for _ in range(size)]

# Generates an array of random numbers with a length the user specifies and sorts them using insertion sort.
# It will print the sorted array if the user provides an extra arguement.
if __name__ == "__main__":
    size = int(sys.argv[1])
    A = generate_large_array(size)
    A = quicksort(A)

    if len(sys.argv) == 3:
        print(A)