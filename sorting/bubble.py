import random
import sys

# Bubble sort implementation. Runtime: O(n^2).
def bubbleSort(A: list) -> list:
    for i in range(0, len(A)):
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

# Generates an array of random numbers with a size of size.
def generate_large_array(size: int) -> list:
    return [random.randint(0, size) for _ in range(size)]

# Generates an array of random numbers with a length the user specifies and sorts them using bubblesort.
# It will print the sorted array if the user provides an extra arguement.
if __name__ == "__main__":
    size = int(sys.argv[1])
    A = generate_large_array(size)

    A = bubbleSort(A)

    if len(sys.argv) == 3:
        print(A)