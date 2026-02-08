import numpy as np
from datasets import datasetA, datasetD
from output_sensitive import output_sensitive_hull
from sweeping import is_clockwise, sweeping_algorithm

algorithms = [sweeping_algorithm, output_sensitive_hull]

def test_is_clockwise():
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

def test_algorithm_datasetA(n = 10000):
    for algorithm in algorithms:
        for i in range(100):
            print(i)
            points = datasetA(n)
            assert algorithm(points).shape[0] == 5  # Start and end points are the same

def test_algorithm_datasetD(n = 10000):
    for algorithm in algorithms:
        for i in range(100):
            print(i)
            points = datasetD(n)
            assert algorithm(points).shape[0] == n+1

if __name__ == "__main__":
    test_is_clockwise()
    test_algorithm_datasetA()
    test_algorithm_datasetD()