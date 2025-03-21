import random
import sys

# Implements quick sort using a random selection of the pivot value. Runtime: O(nlogn)
def randomQuicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    # Randomly select a pivot
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right partitions, then combine
    return randomQuicksort(left) + middle + randomQuicksort(right)

# Generates an array of random numbers with a size of size.
def generate_large_array(size: int) -> list:
    return [random.randint(0, size) for _ in range(size)]

# Generates an array of random numbers with a length the user specifies and sorts them using insertion sort.
# It will print the sorted array if the user provides an extra arguement.
if __name__ == "__main__":
    size = int(sys.argv[1])
    A = generate_large_array(size)
    A = randomQuicksort(A)

    if len(sys.argv) == 3:
        print(A)