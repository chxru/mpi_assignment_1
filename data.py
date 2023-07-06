import csv
import random
import os


def generate_data(students: int):
    """
    Create a csv for the number of students
    """
    if os.path.exists("data.csv"):
        os.remove("data.csv")

    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        # writer.writerow(['Student', 'Maths', 'English', 'DSA', 'HPC'])
        for i in range(1, students + 1):
            writer.writerow(
                [
                    i,
                    random.randint(0, 100),
                    random.randint(0, 100),
                    random.randint(0, 100),
                    random.randint(0, 100),
                ]
            )
