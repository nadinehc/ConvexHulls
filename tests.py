import numpy as np
import matplotlib.pyplot as plt
from datasets import datasetA, datasetB,  datasetC, datasetD
from output_sensitive import output_sensitive_algorithm
from sweeping import is_clockwise, sweeping_algorithm
from output_sensitive import median

algorithms = [sweeping_algorithm, output_sensitive_algorithm]

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

def test_algorithm_datasetA(n = 10000):
    for algorithm in algorithms:
        for i in range(100):
            print(i)
            points = datasetA(n)
            assert algorithm(points).shape[0] == 5  # Start and end points are the same

def test_algorithm_datasetD(n = 10000):
    for algorithm in algorithms:
        for i in range(100):
            print(i)
            points = datasetD(n)
            assert algorithm(points).shape[0] == n+1

if __name__ == "__main__":
    test_is_clockwise()
    test_algorithm_datasetA()
    test_algorithm_datasetD()


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
