import matplotlib.pyplot as plt
import csv
import numpy as np

def create_data(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            for i, value in enumerate(row):
                if len(data) <= i:
                    data.append([])
                try:
                    data[i].append(float(value))
                except ValueError:
                    data[i].append(value)
    return data

def draw_graph(data):
    # Sort data based on x values
    sorted_data = sorted(zip(*data))
    data = list(zip(*sorted_data))

    for i in range(1, len(data)):
        plt.plot(data[0], data[i], linestyle='dashed', marker='o', label=f"Value {i}")

    y_values = set()
    for i in range(1, len(data)):
        y_values.update(data[i])

    y_labels = [str(int(y)) if y.is_integer() else str(y) for y in sorted(y_values)]
    plt.yticks(sorted(y_values), y_labels, fontsize=12)  # Increase font size

    x_values = data[0]
    x_labels = [str(int(x)) if x.is_integer() else str(x) for x in x_values]
    plt.xticks(x_values, x_labels, fontsize=12, rotation=25)  # Increase font size and rotate

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('GraphDynamics', fontsize=20)
    plt.grid()
    plt.legend()
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()