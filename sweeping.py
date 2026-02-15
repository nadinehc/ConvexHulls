import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from utils import is_clockwise

from datasets import datasetA, datasetB, datasetC, datasetD

def sweeping_algorithm(points: np.ndarray, return_all_steps=False) -> np.ndarray:
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
    
    all_steps = []

    # preprocessing : sort points by x-coordinate
    sorted_indices = np.argsort(points[:, 0])
    sorted_points = points[sorted_indices]

    convex_hull = [sorted_points[0], sorted_points[1]]

    # visualize the state of the hull at each step
    if return_all_steps:
        all_steps.append(np.array(convex_hull))

    # upper hull
    for i in range(2, len(sorted_points)):
        while len(convex_hull) > 1 and is_clockwise(convex_hull[-1], convex_hull[-2], sorted_points[i]):
            convex_hull.pop(-1)

        convex_hull.append(sorted_points[i])

        if return_all_steps:
            all_steps.append(np.array(convex_hull))

    # lower hull
    convex_hull.append(sorted_points[-2])
    
    if return_all_steps:
        all_steps.append(np.array(convex_hull))

    for i in range(len(sorted_points) - 3, -1, -1):
        while len(convex_hull) > 1 and is_clockwise(convex_hull[-1], convex_hull[-2], sorted_points[i]):
            convex_hull.pop(-1)

        convex_hull.append(sorted_points[i])

        if return_all_steps:
            all_steps.append(np.array(convex_hull))

    if return_all_steps:
        return all_steps
    return np.array(convex_hull)

def generate_video_sweeping(n, dataset="A", filename="convex_hull.gif"):
    """
    Generates a video of the sweeping algorithm in action.

    Args:
        points (np.ndarray): set of points in the 2D plane
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
    all_steps = sweeping_algorithm(points, return_all_steps=True)

    fig, ax = plt.subplots()
    ax.scatter(points[:, 0], points[:, 1], color='blue')
    line, = ax.plot([], [], color='red')

    def update(frame):
        hull = all_steps[frame]
        line.set_data(hull[:, 0], hull[:, 1])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=len(all_steps), blit=True, repeat=False)
    ani.save("convex_hull.gif", writer="pillow")
    plt.show()