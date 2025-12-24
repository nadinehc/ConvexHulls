from sweeping import is_clockwise
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