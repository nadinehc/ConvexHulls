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
    X = np.random.rand(n-4, 2)
    corners = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    X = np.vstack([X, corners])
    angle = np.random.rand() * (2 * np.pi)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    X = (X - 0.5) @ rotation_matrix.T + 0.5
    indices = np.random.permutation(n)
    X = X[indices]
    return X

def datasetB(n: int):
    """
    Generates n samples randomly distributed in the unit square.
    """
    X = np.random.rand(n, 2)
    return X 

def datasetC(n: int):
    """
    Generates n samples randomly distributed in the disk 
    centered at (1/2, 1/2) with radius 1/2.
    """
    r = np.sqrt(np.random.rand(n)) / 2
    theta = np.random.rand(n) * (2 * np.pi)
    X = np.column_stack([r * np.cos(theta), r * np.sin(theta)])
    X += 0.5  # Shift the center to (0.5, 0.5)
    return X

def datasetD(n: int):
    """
    Generates dataset D with n samples distributed on the circle centered at (1/2, 1/2) with radius 1/2.
    """
    theta = np.random.rand(n) * (2 * np.pi)
    X = np.column_stack([0.5 * np.cos(theta), 0.5 * np.sin(theta)])
    X += 0.5  # Shift the center to (0.5, 0.5)
    return X

def visualize_dataset():
    """
    Visualizes the dataset using a scatter plot.
    """
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.3)

    square_x = [0, 1, 1, 0, 0]
    square_y = [0, 0, 1, 1, 0]

    # Circle
    theta = np.linspace(0, 2*np.pi, 400)

    x = 0.5 * np.cos(theta) + 0.5
    y = 0.5 * np.sin(theta) + 0.5

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