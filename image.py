import matplotlib.pyplot as plt
import numpy as np
from datasets import datasetA, datasetB, datasetC, datasetD
from kirkpatrick_seidel import find_line, median

def image():
    """
    visualizes the convex hull for one of the datasets A, B, C, D

    Args:
        dataset (str, optional): dataset to visualize. Defaults to "A". Possible values are "A", "B", "C", "D".
    """
    
    
    points = datasetB(50)
    P = [point.tolist() for point in points]
    m = median(P)
    p1, p2 = find_line(P,m)
    right_points = []
    left_points = []
    others = []
    for point in P:
        if point[0] <= p1[0]: 
            left_points.append(point) 
        elif point[0] >= p2[0]:
            right_points.append(point)
        else :
            others.append(point)

    left_points = np.array(left_points)
    right_points = np.array(right_points)
    others = np.array(others)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot()

    ax.scatter(left_points[:, 0], left_points[:, 1], color='blue')
    ax.scatter(right_points[:, 0], right_points[:, 1], color='green')
    ax.scatter(others[:, 0], others[:, 1], color='orange')


    hull = [p1,p2]
    hull = np.array(hull)
    
    ax.plot(hull[:, 0], hull[:, 1], color='red')
    plt.show()