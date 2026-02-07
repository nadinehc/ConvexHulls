import numpy as np
from sweeping import is_clockwise

def gift_wrapping_algorithm(points: np.ndarray) -> np.ndarray:
    """Implement the gift wrapping algorithm (also known as Jarvis March)
    - start from the leftmost point
    - at each step, select the point that makes the smallest angle with the last edge of the hull

    Args:
        points (np.ndarray): set of points in the 2D plane

    Returns:
        np.ndarray: the convex hull of the input points as an array of points
    """
    if points.size < 3:
        return points
    
    leftmost_index = np.argmin(points[:, 0])
    hull = [points[leftmost_index]]
    p = leftmost_index

    while True:
        q = 0
        if q == p:
            q = 1
        for i in range(q+1, len(points)):
            if is_clockwise(points[p], points[i], points[q]):
                q = i
        hull.append(points[q])
        p = q
        if p == leftmost_index:
            break

    return np.array(hull)