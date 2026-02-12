import matplotlib.pyplot as plt
import numpy as np
import time
from datasets import datasetA, datasetB, datasetC, datasetD
from sweeping import sweeping_algorithm
from kirkpatrick_seidel import kirkpatrick_seidel_algorithm, median 
from gift_wrapping import gift_wrapping_algorithm
from quick_hull import quick_hull_algorithm



def execution_time(algorithm, points):
    
    start = time.process_time()
    algorithm(points)
    end = time.process_time()

    return end-start


def execution_time_comparison(dataset = "B", gift_wrapping = False, quick_hull = False):
    N = np.linspace(1000,10000,10, dtype=int)
    
    dataset_map = {
        "A": datasetA,  
        "B": datasetB,  
        "C": datasetC,  
        "D": datasetD,  
    } 
    
    if dataset not in dataset_map:
        raise ValueError(f"Invalid dataset '{dataset}'. Choose from 'A', 'B', 'C', 'D'.")

    t1 = [0 for n in N]
    t2 = [0 for n in N]
    if gift_wrapping:
        t3 = [0 for n in N]
    if quick_hull:
        t4 = [0 for n in N]

    for i in range(len(N)):
        points = dataset_map[dataset](N[i])
        t1[i] = execution_time(sweeping_algorithm, points)
        t2[i] = execution_time(kirkpatrick_seidel_algorithm, points)
        if gift_wrapping:
            t3[i] = execution_time(gift_wrapping_algorithm, points)
        if quick_hull:
            t4[i] = execution_time(quick_hull_algorithm, points)


    plt.figure(figsize=(9, 5))
    plt.plot(N, t1, label = "Sweeping Algorithm", color = 'blue', marker='o')
    plt.plot(N, t2, label = "Kirkpatrick Seidel Algorithm", color = 'red', marker='o')
    if gift_wrapping:
        plt.plot(N, t3, label = "Gift Wrapping Algorithm", color = 'green', marker='o')
    if quick_hull:
        plt.plot(N, t4, label = "Quick Hull Algorithm", color = 'orange', marker='o')


    #plt.plot(N, N*np.log(N)*t1[0]/20000, color = "grey")
    plt.xlabel("Number of points")
    plt.ylabel("Execution time (seconds)")
    plt.legend()
    plt.title("Execution Time Comparison (Dataset "+ dataset+ ")")
    plt.tight_layout()
    plt.show()


def hull_comparison(n, dataset="A"):
    dataset_map = {
        "A": datasetA,  
        "B": datasetB,  
        "C": datasetC,  
        "D": datasetD,  
    }

    if dataset not in dataset_map:
        raise ValueError(f"Invalid dataset '{dataset}'. Choose from 'A', 'B', 'C', 'D'.")
    
    points = dataset_map[dataset](n)
    hull1 = sweeping_algorithm(points)
    hull2 = kirkpatrick_seidel_algorithm(points)
    hull3 = gift_wrapping_algorithm(points)
    hull4 = quick_hull_algorithm(points)

    fig, ax = plt.subplots(2,2)

    for i in range(2):
        for j in range(2):

            ax[i][j].scatter(points[:, 0], points[:, 1], color='blue')
            ax[i][j].set_aspect("equal")
    

    ax[0][0].plot(hull1[:, 0], hull1[:, 1], color='red')
    ax[0][1].plot(hull2[:, 0], hull2[:, 1], color='red') 
    ax[1][0].plot(hull1[:, 0], hull3[:, 1], color='red')
    ax[1][1].plot(hull2[:, 0], hull4[:, 1], color='red') 

    ax[0][0].set_title("Sweeping Algorithm")
    ax[0][1].set_title("Kirkpatrick Seidel Algorithm")  
    ax[1][0].set_title("Gift Wrapping Algorithm")
    ax[1][1].set_title("Quick Hull Algorithm")  

    fig.suptitle("Convex Hull Comparison") 
    plt.tight_layout()
    plt.show()


def nb_recursive_call_median(nb_points, nb_runs, dataset, max_iter=50):
    
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


def nb_recursive_call_graph(nb_points, nb_runs=100, dataset="B"):
    iterations, freq = nb_recursive_call_median(nb_points, nb_runs, dataset)

    plt.figure(figsize=(8, 4))

    plt.bar(iterations,freq,alpha=0.8)

    plt.xlabel("Number of recursive calls")
    plt.ylabel("Frequency")
    plt.title(f"Number of recursive calls in the find function used by the median function (N = {nb_points})")
    plt.xlim(0, 10)
    plt.xticks(np.arange(1, 10))
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


