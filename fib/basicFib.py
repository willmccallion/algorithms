import sys 

# Recursive fibonacci function. Runtime: O(2^n).
def fib(n: int) -> int:
    if n < 2:
        return n
    
    return fib(n - 1) + fib(n - 2)

# Finds the fib(n) that the user inputs and prints if they request
if __name__ == "__main__":
    fib = fib(int(sys.argv[1]))

    if len(sys.argv) == 3:
        print(fib)