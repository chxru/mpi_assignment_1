import time
import sys
import numpy as np
from mpi4py import MPI
from data import generate_data
from helper import get_average_marks

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def main():
    total_students = int(sys.argv[1])
    if total_students <= 0:
        print("Number of students must be greater than 0")
        sys.exit(1)

    sendbuf = None
    padded_student_count = size - total_students % size

    """
    Why padding?

    When using scatter or scatterv, if the number of elements in the send buffer is not divisble by the number of processes,
    1. When dividing the buffer into equal parts, some buffers will have half of the data of an array while some other processor will receive the remaining half.
    2. Last buffer will have less data than the other buffers, the remaining data will be filled with garbage values. This can be avoided by sending the expected number of elements to each process.

    Solution:
    Add empty elements to the array until the number of elements is divisible by the number of processes!
    """

    if rank == 0:
        # generate the data
        generate_data(total_students)

        sendbuf = np.genfromtxt("data.csv", delimiter=",", dtype=int)

        # if the number of students is not divisible by the number of processes
        # then we need to pad the data with 0s
        if total_students % size != 0:
            padding = np.zeros((size - total_students % size, 5), dtype=int)
            sendbuf = np.concatenate((sendbuf, padding))

    recvbuf = np.empty(((total_students + padded_student_count) // size, 5), dtype=int)
    comm.Scatterv(sendbuf, recvbuf, root=0)

    start_time = time.time()
    # calculate the average marks
    avg = get_average_marks(recvbuf)

    # print(f"Process {rank} calculated {avg}")
    print(time.time() - start_time)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 parallel.py <number of students>")
        sys.exit(1)

    main()
