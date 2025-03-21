import subprocess
import time
import matplotlib.pyplot as plt 
import concurrent.futures
import os
import sys

# Runs and times the program at a specific path.
def runProg(n: int, path: str) -> tuple[int, str]:
    start = time.time()
    result = subprocess.run(["python3", path, str(n)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    elapsed_ms = (time.time() - start) * 1000
    return elapsed_ms, result.stdout.decode().strip()

# Runs the programs in a specific directory with a max n value and max time.
def main():
    # Initial program requirements to test runtimes
    programs = [prog for prog in os.listdir(sys.argv[1]) if prog.endswith('.py')]
    nValues = []
    times = {prog: [] for prog in programs}
    active_programs = set(programs)
    
    max_n = int(sys.argv[2]) if len(sys.argv) > 2 else 100000000
    max_time = int(sys.argv[3]) if len(sys.argv) > 3 else 1000

    start = time.time()

    n = 0
    increment = 1

    # Uses multiple threads to speed up execution
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Makes sure n is less than max n and there are still programs that have not exceeded the time limit
        while n < max_n and active_programs:
            # Runs the programs in parallel to speed up execution time
            futures = {}
            for prog in list(active_programs):
                path = os.path.join(sys.argv[1], prog)
                futures[prog] = executor.submit(runProg, n, path)

            # Gets the length of time each program ran for
            for prog, future in futures.items():
                try:
                    elapsed, _ = future.result(timeout=max_time / 1000)
                    times[prog].append(elapsed)
                    if elapsed > max_time:
                        active_programs.remove(prog)
                except concurrent.futures.TimeoutError:
                    print(f"Program {prog} exceeded max time and was removed.")
                    active_programs.remove(prog)

            # Add the n value to the x axis for plot and print information about the execution of the programs
            nValues.append(n)
            print(f"n = {n}, active programs = {[program for program in active_programs]}")

            # Every minute increase the increment amount of n by a power of 10
            if time.time() - 60 > start:
                start = time.time()
                increment *= 10

            n += increment

    # Create a graph with the results and save it in the directory of the algorithms
    plt.figure(figsize=(10, 6))
    for prog, prog_times in times.items():
        if prog_times:
            plt.plot(nValues[:len(prog_times)], prog_times, linestyle='-', linewidth=0.8, label=prog[:-3])
    plt.xlabel("n")
    plt.ylabel("Execution Time (ms)")
    plt.title("Algorithm Execution Time Comparisons")
    plt.legend()
    plt.grid(True)
    output_dir = sys.argv[1].rstrip('/')
    output_filename = os.path.basename(os.path.normpath(output_dir))
    plt.savefig(os.path.join(output_dir, output_filename))
    plt.show()

if __name__ == "__main__":
    main()
