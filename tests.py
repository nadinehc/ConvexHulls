import numpy as np
import matplotlib.pyplot as plt
from datasets import datasetA, datasetB,  datasetC, datasetD
from sweeping import is_clockwise, sweeping_algorithm
from kirkpatrick_seidel import kirkpatrick_seidel_algorithm
from gift_wrapping import gift_wrapping_algorithm
from quick_hull import quick_hull_algorithm

algorithms = [sweeping_algorithm, kirkpatrick_seidel_algorithm, gift_wrapping_algorithm, quick_hull_algorithm]

def test_is_clockwise():
    print("Testing is_clockwise function...")
    A = np.array([0, 0])
    B = np.array([1, 0])
    C = np.array([0, 1])
    assert is_clockwise(A, B, C) == False  # Counter-clockwise

    A = np.array([0, 0])
    B = np.array([0, 1])
    C = np.array([1, 0])
    assert is_clockwise(A, B, C) == True  # Clockwise

    A = np.array([0, 0])
    B = np.array([1, 1])
    C = np.array([2, 2])
    assert is_clockwise(A, B, C) == False  # Collinear

    A = np.array([0, 0])
    B = np.array([1, 0])
    C = np.array([0, -1])
    assert is_clockwise(A, B, C) == True  # Clockwise

    print("All tests passed for is_clockwise function!")

def test_algorithm_datasetA(n = 10000):
    print("Testing algorithms on dataset A with n=", n)
    print("------------------------------------------")
    for algorithm in algorithms:
        print("Testing ", algorithm.__name__)
        for i in range(100):
            print(i, end="")
            points = datasetA(n)
            assert algorithm(points).shape[0] == 5  # Start and end points are the same
            print(" - Passed")
        print("All tests passed for ", algorithm.__name__)
        print("------------------------------------------")

def test_algorithm_datasetD(n = 100):
    print("Testing algorithms on dataset D with n=", n)
    print("------------------------------------------")
    for algorithm in algorithms:
        print("Testing ", algorithm.__name__)   
        for i in range(100):
            print(i, end="")
            points = datasetD(n)
            assert algorithm(points).shape[0] == n+1
            print(" - Passed")
        print("All tests passed for ", algorithm.__name__)
        print("------------------------------------------")

if __name__ == "__main__":
    test_is_clockwise()
    test_algorithm_datasetA()
    test_algorithm_datasetD()
