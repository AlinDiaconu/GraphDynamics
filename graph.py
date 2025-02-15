import matplotlib.pyplot as plt
import csv

def create_data(file_path):
    x = []
    y = []
    with open(file_path, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))
    return x, y

def draw_graph(x, y):
    plt.plot(x, y, color='g', linestyle='dashed', marker='o', label="Weather Data")
    plt.xticks(rotation=25)
    plt.xlabel('Dates')
    plt.ylabel('Temperature')
    plt.title('Weather Report', fontsize=20)
    plt.grid()
    plt.legend()
    plt.show()