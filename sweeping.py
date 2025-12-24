import numpy as np
import matplotlib.pyplot as plt

from datasets import datasetA, datasetB, datasetC, datasetD

def is_clockwise(A, B, C) -> bool:
    """
    Check if the points A, B, C are in clockwise order.
    """
    AB = B - A
    AC = C - A
    if A[0] != B[0]:
        # cross product
        return AB[0] * AC[1] - AB[1] * AC[0] < 0
    else:
        if A[1] < B[1]:
            return AC[0] > 0
        elif A[1] > B[1]:
            return AC[0] < 0
        else:
            return False  # A and B are the same point
        
def sweeping_algorithm(points: np.ndarray) -> np.ndarray:
    """Implement the sweeping algorithm
    - sort the points according to their x-coordinate
    - compute the upper hull with counter-clockwise turns
    - compute the lower hull with clockwise turns

    Args:
        points (np.ndarray): set of points in the 2D plane

    Returns:
        np.ndarray: the convex hull of the input points as an array of points
    """
    if points.size < 3:
        return points

    # preprocessing : sort points by x-coordinate
    sorted_indices = np.argsort(points[:, 0])
    sorted_points = points[sorted_indices]

    upper_hull = [sorted_points[0], sorted_points[1]]
    i = 2
    while upper_hull[-1][0] != sorted_points[-1][0] and upper_hull[-1][1] != sorted_points[-1][1]:
        while len(upper_hull) > 1 and is_clockwise(upper_hull[-1], upper_hull[-2], sorted_points[i]):
            upper_hull.pop(-1)

        upper_hull.append(sorted_points[i])
        i += 1

    lower_hull = [sorted_points[0], sorted_points[1]]
    i = 2
    while lower_hull[-1][0] != sorted_points[-1][0] and lower_hull[-1][1] != sorted_points[-1][1]:
        while len(lower_hull) > 1 and not is_clockwise(lower_hull[-1], lower_hull[-2], sorted_points[i]):
            lower_hull.pop(-1)

        lower_hull.append(sorted_points[i])
        i += 1

    return np.vstack([upper_hull, lower_hull[::-1][1:]])

def visualize_hull(n, dataset="A"):
    """
    visualizes the convex hull for one of the datasets A, B, C, D

    Args:
        dataset (str, optional): dataset to visualize. Defaults to "A". Possible values are "A", "B", "C", "D".
    """
    dataset_map = {
        "A": datasetA,  
        "B": datasetB,  
        "C": datasetC,  
        "D": datasetD,  
    }

    if dataset not in dataset_map:
        raise ValueError(f"Invalid dataset '{dataset}'. Choose from 'A', 'B', 'C', 'D'.")
    
    points = dataset_map[dataset](n)
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot()
    ax.scatter(points[:, 0], points[:, 1], color='blue')

    hull = sweeping_algorithm(points)
    ax.plot(hull[:, 0], hull[:, 1], color='red')
    plt.show()