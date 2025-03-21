import sys

# Linear fibonacci function. Runtime: O(n).
def fib(n: int) -> int:
    A = [0, 1]

    for i in range(2,(n+1)):
        A.append(A[i-1] + A[i-2])

    return A[n]

# Finds the fib(n) that the user inputs and prints if they request
if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    fib = fib(int(sys.argv[1]))

    if len(sys.argv) == 3:
        print(fib)