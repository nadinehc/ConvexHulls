from sweeping import sweeping_algorithm
import matplotlib.pyplot as plt
from datasets import datasetA, datasetB, datasetC, datasetD

def visualize_hull(n, dataset="A", algorithm=sweeping_algorithm):
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

    hull = algorithm(points)
    ax.plot(hull[:, 0], hull[:, 1], color='red')
    plt.show()