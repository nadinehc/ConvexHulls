from utils import is_clockwise
import numpy as np
import matplotlib.pyplot as plt

def quick_hull_up(p_left, p_right, points, steps=None):
    if len(points) == 0:
        return []

    up = max(points, key=lambda p: distance_to_line(p, p_left, p_right))

    if steps is not None:
        steps.append((p_left, up, p_right))

    set1 = [p for p in points if p is not up and is_clockwise(p_left, p, up)]
    set2 = [p for p in points if p is not up and is_clockwise(up, p, p_right)]
 
    return quick_hull_up(p_left, up, set1, steps) + [up] + quick_hull_up(up, p_right, set2, steps)

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

def quick_hull_algorithm(points, visualize=False):
    steps = [] if visualize else None

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

    hull = [p_left] + quick_hull_up(p_left, p_right, above, steps) + [p_right] + quick_hull_up(p_right, p_left, below, steps) + [p_left]

    if visualize:
        n = len(steps) + 1
        # Determine grid size
        cols = int(np.ceil(np.sqrt(n)))
        rows = int(np.ceil(n / cols))
        
        _, axes = plt.subplots(rows, cols, figsize=(cols*4, rows*4))
        axes = np.atleast_1d(axes).flatten() # Handles single or multiple subplots
        
        axes[0].set_aspect("equal")
        axes[0].set_title("Starting line")
        axes[0].scatter(points[:, 0], points[:, 1], color='blue', s=10)
        axes[0].plot([p_left[0], p_right[0]], [p_left[1], p_right[1]], 'r--')

        # Track the lines we've already drawn to carry them over to the next plot
        history = [[p_left[0], p_right[0]], [p_left[1], p_right[1]]]

        for i, step in enumerate(steps):
            ax = axes[i+1]
            ax.set_aspect("equal")
            ax.set_title(f"Step {i+1}")
            
            ax.scatter(points[:, 0], points[:, 1], color='blue', s=10)
            
            p_left, up, p_right = step
            history.append(([p_left[0], up[0], p_right[0]], [p_left[1], up[1], p_right[1]]))
            
            for h_x, h_y in history:
                ax.plot(h_x, h_y, 'r-' if i == len(steps)-1 else 'r--')

        # Hide any unused subplots
        for j in range(i + 2, len(axes)):
            axes[j].axis('off')

        plt.tight_layout()

        plt.savefig("quick_hull_steps.png")

        # plt.show()

    return np.array(hull)