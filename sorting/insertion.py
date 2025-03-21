import random 
import sys

# Implementation of insertion sort. Runtime: O(n^2).
def insertion(A: list) -> list:
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        
        A[j+1] = key

    return A

# Generates an array of random numbers with a size of size.
def generate_large_array(size: int) -> list:
    return [random.randint(0, size - 1) for _ in range(size)]

# Generates an array of random numbers with a length the user specifies and sorts them using insertion sort.
# It will print the sorted array if the user provides an extra arguement.
if __name__ == "__main__":
    size = int(sys.argv[1])
    A = generate_large_array(size)
    A = insertion(A)

    if len(sys.argv) == 3:
        print(A)