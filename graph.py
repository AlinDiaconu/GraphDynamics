import matplotlib.pyplot as plt
import csv

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
    for i in range(1, len(data)):
        plt.plot(data[0], data[i], linestyle='dashed', marker='o', label=f"Value {i}")
    plt.xticks(rotation=25)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('GraphDynamics', fontsize=20)
    plt.grid()
    plt.legend()
    plt.show()