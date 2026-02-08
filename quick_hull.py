from utils import is_clockwise
import numpy as np

def quick_hull_up(p_left, p_right, points):
    if len(points) == 0:
        return []

    up = max(points, key=lambda p: distance_to_line(p, p_left, p_right))
    set1 = [p for p in points if p is not up and is_clockwise(p_left, p, up)]
    set2 = [p for p in points if p is not up and is_clockwise(up, p, p_right)]
 
    return quick_hull_up(p_left, up, set1) + [up] + quick_hull_up(up, p_right, set2)



def distance_to_line(P, A, B):
    """Calculate the distance from a point to a line defined by two points

    Args:
        P (np.ndarray): the point to calculate the distance from
        A (np.ndarray): the starting point of the line
        B (np.ndarray): the ending point of the line
    Returns:
        float: the distance from P to the line (AB)
    """
    if A[0] == B[0]:  # vertical line
        return abs(P[0] - A[0]) 
    
    AP = P - A
    AB = B - A
    return abs(AB[0] * AP[1] - AB[1] * AP[0]) / np.linalg.norm(AB)

def quick_hull(points):
    # find point with minimum and maximum x coordinate
    p_left = points[0]
    p_right = points[0]
    for point in points:
        if point[0] < p_left[0] or (point[0] == p_left[0] and point[1] < p_left[1]):
            p_left = point
        if point[0] > p_right[0] or (point[0] == p_right[0] and point[1] > p_right[1]):
            p_right = point

    # split points into two sets: those above the line p_left-p_right and those below
    above = []
    below = []
    for point in points:
        if is_clockwise(p_left, point, p_right):
            above.append(point)
        if is_clockwise(p_right, point, p_left):
            below.append(point)

    hull = [p_left] + quick_hull_up(p_left, p_right, above) + [p_right] + quick_hull_up(p_right, p_left, below) + [p_left]

    return np.array(hull)