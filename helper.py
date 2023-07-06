import numpy as np


def get_average_marks(data: np.ndarray) -> list[(str, int)]:
    """
    Get the average marks of each student
    """
    result: list[(str, int)] = []
    for i in data:
        student = i[0]
        marks = [int(j) for j in i[1:]]

        average = sum(marks) / len(marks)

        result.append((student, average))

    return result
