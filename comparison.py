import matplotlib.pyplot as plt
import numpy as np
import time

from sweeping import sweeping_algorithm
from output_sensitive import output_sensitive_algorithm 
from datasets import datasetA, datasetB, datasetC, datasetD

def execution_time(algorithm, points):
    
    start = time.process_time()
    algorithm(points)
    end = time.process_time()

    return end-start


def execution_time_comparison(dataset = "B"):
    N = np.linspace(10000,100000,10, dtype=int)
    #N = np.array([10000,20000,30000,40000,50000])
    
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
    
    for i in range(len(N)):
        points = dataset_map[dataset](N[i])
        t1[i] = execution_time(sweeping_algorithm, points)
        t2[i] = execution_time(output_sensitive_algorithm, points)


    plt.figure(figsize=(9, 5))

    plt.plot(N, t1, label = "Sweeping Algorithm", color = 'blue', marker='o')
    plt.plot(N, t2, label = "Output-Sensitive Algorithm", color = 'red', marker='s')
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
    hull2 = output_sensitive_algorithm(points)

    fig, (ax1, ax2) = plt.subplots(1,2)


    ax1.scatter(points[:, 0], points[:, 1], color='blue')
    ax2.scatter(points[:, 0], points[:, 1], color='blue')

    ax1.plot(hull1[:, 0], hull1[:, 1], color='red')
    ax2.plot(hull2[:, 0], hull2[:, 1], color='red') 

    ax1.set_title("Sweeping Algorithm")
    ax2.set_title("Output-Sensitive Algorithm")  

    ax1.set_aspect("equal")
    ax2.set_aspect("equal")

    fig.suptitle("Convex Hull Comparison") 

    plt.show()




