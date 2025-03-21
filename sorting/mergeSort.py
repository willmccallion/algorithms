import random
import sys

# Function to merge a list A using the low, mid, and high values of it. Runtime: O(n).
def merge(A: list, low: int, mid: int, high: int):
    B = A[low:mid + 1]
    C = A[mid + 1:high + 1]

    i = 0
    j = 0
    k = low

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1

    while i < len(B):
        A[k] = B[i]
        i += 1
        k += 1

    while j < len(C):
        A[k] = C[j]
        j += 1
        k += 1

# Implementation of merge sort function. Runtime: O(nlogn).
def mergeSort(A: list):
    n = len(A)
    current_size = 1

    while current_size < n:
        for low in range(0, n, 2 * current_size):
            mid = min(low + current_size - 1, n - 1)
            high = min(low + 2 * current_size - 1, n - 1)
            merge(A, low, mid, high)
        current_size *= 2

# Generates an array of random numbers with a size of size.
def generate_large_array(size: int) -> list:
    return [random.randint(0, size) for _ in range(size)]

# Generates an array of random numbers with a length the user specifies and sorts them using insertion sort.
# It will print the sorted array if the user provides an extra arguement.
if __name__ == "__main__":
    size = int(sys.argv[1])
    A = generate_large_array(size)
    mergeSort(A)
    
    if len(sys.argv) == 3:
        print(A)
