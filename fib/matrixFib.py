from functools import lru_cache
import sys

# Matrix calculation of fibonacci number. Runtime: O(logn).
@lru_cache(None)
def fib(n: int) -> int:
    if n < 2:
        return n
    if n & 1:
        k = (n+1) // 2
        return fib(k) ** 2 + fib(k-1) ** 2
    else:
        k = n // 2
        return fib(k) * (2 * fib( k - 1) + fib(k))

# Finds the fib(n) that the user inputs and prints if they request
if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    fib = fib(int(sys.argv[1]))

    if len(sys.argv) == 3:
        print(fib)