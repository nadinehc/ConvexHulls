import matplotlib.pyplot as plt
from datasets import datasetA, datasetB, datasetC, datasetD
import numpy as np
from kirkpatrick_seidel import median

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

def visualize_hull(n, algorithm, dataset="A"):
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

def nb_loop_median(nb_points, nb_runs, dataset, max_iter=50):
    
    freq = np.zeros(max_iter)
    
    dataset_map = {
        "A": datasetA,  
        "B": datasetB,  
        "C": datasetC,  
        "D": datasetD,  
    } 
    
    if dataset not in dataset_map:
        raise ValueError(f"Invalid dataset '{dataset}'. Choose from 'A', 'B', 'C', 'D'.")

    for _ in range(nb_runs):
        points = dataset_map[dataset](nb_points)
        points = [p.tolist() for p in points]
        k = median(points, test_mode = True)
        freq[k] += 1

    freq = freq / nb_runs
    iterations = np.arange(max_iter)

    return iterations, freq


def nb_loop_graph(nb_points, nb_runs=100, dataset="B"):
    iterations, freq = nb_loop_median(nb_points, nb_runs, dataset)

    plt.figure(figsize=(8, 4))

    plt.bar(iterations,freq,alpha=0.8)

    plt.xlabel("Nombre d'itérations de la boucle")
    plt.ylabel("Fréquence")
    plt.title(f"Distribution du nombre d'itérations (N = {nb_points})")
    plt.xlim(0, 10)
    plt.xticks(np.arange(1, 10))
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()