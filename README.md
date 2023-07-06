# MPI Assignment 1

## How to run

1. Make sure python and mpi is installed on your machine.
2. (optional) `python3 -m venv .venv`
3. `pip3 install -r requirements.txt`
4. `python3 main.py`

## Task

### Problem Description

Write an MPI program to calculate the average of student grades for each subject they sit in the final exam. The class consists of 50 students, and each student takes the following subjects: Mathematics, English, Data Structures and Algorithms, and High Performance Computing.  
The grades are numeric, ranging from 0 to 100, and each student is assigned random marks within this range. The task is to write programs as instructed below.

### Problem Instruction

1. Write a sequential program to calculate the average marks per subject.

2. Write an MPI program to run this program in parallel, utilizing 4 processes. The objective is to achieve faster calculation compared to the sequential program.

3. To observe the speed-up, increase the number of students to 10,000 or 100,000 and check if there is a noticeable improvement in performance.

4. Draw a chart showing the speed-up by varying the number of students, calculated as the ratio of sequential processing time to parallel processing time.
