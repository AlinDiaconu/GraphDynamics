import matplotlib.pyplot as plt
import numpy as np


def create_data():
    x = np.linspace(0, 100, 100)
    y1 = np.exp(x / 3)  # Increasing graph
    y2 = np.exp(-x / 3)  # Decreasing graph
    return x, y1, y2


def draw_graph(x, y1, y2):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label='Increasing', color='blue')
    plt.plot(x, y2, label='Decreasing', color='red')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Increasing and Decreasing Graphs')
    plt.legend()
    plt.grid()
    plt.show()
