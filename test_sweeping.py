from datasets import datasetA, datasetD
from sweeping import is_clockwise, sweeping_algorithm
import numpy as np

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

def test_sweeping_algorithm_datasetA(n = 10000):
    for _ in range(10):
        points = datasetA(n)
        assert sweeping_algorithm(points).shape[0] == 5  # Start and end points are the same

def test_sweeping_algorithm_datasetD(n = 10000):
    for _ in range(10):
        points = datasetD(n)
        assert sweeping_algorithm(points).shape[0] == n+1