from graph import create_data, draw_graph

if __name__ == "__main__":
    file_path = 'data.csv'
    x, y = create_data(file_path)
    draw_graph(x, y)