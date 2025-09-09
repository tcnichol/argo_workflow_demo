import time
import sys

def run_tests(num_runs=10):
    for i in range(num_runs):
        print(f"Running test {i + 1}/{num_runs}")
        time.sleep(10)
    print("All tests completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            num_runs = int(sys.argv[1])
            run_tests(num_runs)
        except ValueError:
            print("Please provide a valid integer for the number of runs.")
            sys.exit(1)
    else:
        run_tests()