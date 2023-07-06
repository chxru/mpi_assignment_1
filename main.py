import subprocess
import matplotlib.pyplot as plt

INSTANCES = [50, 100, 200, 500, 1000, 2000, 5000, 10_000, 100_000]
PARALLEL_PROCESSORS = [2, 4, 6]

RESULTS = {}
RESULTS["sequential"] = {}
RESULTS["parallel"] = {}


def run_sequential(students: int) -> float:
    output = subprocess.run(
        ["python3", "sequential.py", str(students)], capture_output=True
    )

    return float(output.stdout.decode("utf-8"))


def run_parallel(processes: int, students: int) -> float:
    output = subprocess.run(
        ["mpirun", "-n", str(processes), "python3", "parallel.py", str(students)],
        capture_output=True,
    )
    output = output.stdout.decode("utf-8").split("\n")

    values = []
    for line in output:
        # escape empty lines
        if line == "":
            continue

        values.append(float(line))

    # average the values
    return sum(values) / len(values)


def plot_results():
    plt.plot(INSTANCES, RESULTS["sequential"].values(), label="sequential")
    plt.plot(
        INSTANCES,
        [RESULTS["parallel"][(i, 2)] for i in INSTANCES],
        label="parallel (2)",
    )
    plt.plot(
        INSTANCES,
        [RESULTS["parallel"][(i, 4)] for i in INSTANCES],
        label="parallel (4)",
    )
    plt.plot(
        INSTANCES,
        [RESULTS["parallel"][(i, 6)] for i in INSTANCES],
        label="parallel (6)",
    )
    plt.legend()
    plt.xlabel("Number of students")
    plt.ylabel("Time (s)")
    plt.show()
    plt.savefig("results.png")


def show_performance_gain():
    # considering the sequential as the baseline
    for i in INSTANCES:
        print(f"Performance gain for {i} students")

        base = RESULTS["sequential"][i]

        for j in PARALLEL_PROCESSORS:
            parallel = RESULTS["parallel"][(i, j)]
            print(f"Performance gain with {j} processes: {base / parallel} times")

        print("\n")


def main():
    for i in INSTANCES:
        print(f"Running sequential for {i} students")
        RESULTS["sequential"][i] = run_sequential(i)

    for i in INSTANCES:
        for j in PARALLEL_PROCESSORS:
            print(f"Running parallel for {i} students and {j} processors")
            RESULTS["parallel"][(i, j)] = run_parallel(j, i)

    show_performance_gain()
    plot_results()


if __name__ == "__main__":
    main()
