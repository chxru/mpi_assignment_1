import time
import sys
import numpy as np
from data import generate_data
from helper import get_average_marks


def main():
    n_students = int(sys.argv[1])
    if n_students <= 0:
        print("Number of students must be greater than 0")
        sys.exit(1)

    generate_data(n_students)

    rows = np.genfromtxt("data.csv", delimiter=",", dtype="unicode")

    start_time = time.time()
    get_average_marks(rows)
    print(time.time() - start_time)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 sequential.py <number of students>")
        sys.exit(1)

    main()
