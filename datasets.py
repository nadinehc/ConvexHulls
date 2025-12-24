import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

def datasetA(n: int):
    """
    - Generates n-4 samples randomly distributed in the unit square.
    - Adds 4 corner points.
    - Rotate the whole dataset by a random angle.
    - Shuffle the dataset.
    """
    X = np.random.rand(n-4, 2) * 2 - 1
    corners = np.array([[-1, -1], [1, -1], [-1, 1], [1, 1]])
    X = np.vstack([X, corners])
    angle = np.random.rand() * (2 * np.pi)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    X = X @ rotation_matrix.T
    indices = np.random.permutation(n)
    X = X[indices]
    return X

def datasetB(n: int):
    """
    Generates n samples randomly distributed in the unit square.
    """
    X = np.random.rand(n, 2) * 2 - 1
    return X 

def datasetC(n: int):
    """
    Generates n samples randomly distributed in the unit disk.
    """
    r = np.sqrt(np.random.rand(n))
    theta = np.random.rand(n) * (2 * np.pi)
    X = np.column_stack([r * np.cos(theta), r * np.sin(theta)])
    return X

def datasetD(n: int):
    """
    Generates dataset D with n samples distributed in a circular pattern.
    """
    theta = np.random.rand(n) * (2 * np.pi)
    X = np.column_stack([np.cos(theta), np.sin(theta)])
    return X

def visualize_dataset():
    """
    Visualizes the dataset using a scatter plot.
    """
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.3)

    square_x = [-1, 1, 1, -1, -1]
    square_y = [-1, -1, 1, 1, -1]

    # Circle
    theta = np.linspace(0, 2*np.pi, 400)

    x = np.cos(theta)
    y = np.sin(theta)

    datasets = {
        "A": datasetA,
        "B": datasetB,
        "C": datasetC,
        "D": datasetD
    }

    rax = plt.axes([0.05, 0.4, 0.15, 0.2])
    radio = RadioButtons(rax, list(datasets.keys()))

    def update(label):
        ax.clear()
        X = datasets[label](50)
        ax.scatter(X[:,0], X[:,1], s=5)
        ax.plot(x, y, linewidth=1, linestyle='--', color='gray')
        ax.plot(square_x, square_y, linewidth=1, linestyle='--', color='gray')
        ax.set_title(label)
        ax.set_xlim([-1.5, 1.5])
        ax.set_ylim([-1.5, 1.5])
        ax.axis('equal')
        fig.canvas.draw_idle()

    radio.on_clicked(update)
    update(list(datasets.keys())[0])

    plt.show()