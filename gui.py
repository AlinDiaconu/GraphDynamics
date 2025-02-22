import tkinter as tk
from tkinter import messagebox
from graph import deseneaza_grafic

class DataEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Introducere Date pentru Grafic")

        self.entries = []
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Nume").grid(row=0, column=0)
        tk.Label(frame, text="Valoare x").grid(row=0, column=1)
        tk.Label(frame, text="Valoare y").grid(row=0, column=2)

        self.add_entry_row(frame)

        add_button = tk.Button(self.root, text="Adaugă rând", command=lambda: self.add_entry_row(frame))
        add_button.pack(pady=5)

        plot_button = tk.Button(self.root, text="Desenează grafic", command=self.plot_graph)
        plot_button.pack(pady=5)

    def add_entry_row(self, frame):
        row = len(self.entries) + 1
        name_entry = tk.Entry(frame)
        x_entry = tk.Entry(frame)
        y_entry = tk.Entry(frame)
        delete_button = tk.Button(frame, text="Șterge", command=lambda: self.delete_entry_row(row))

        name_entry.grid(row=row, column=0, padx=5, pady=5)
        x_entry.grid(row=row, column=1, padx=5, pady=5)
        y_entry.grid(row=row, column=2, padx=5, pady=5)
        delete_button.grid(row=row, column=3, padx=5, pady=5)

        self.entries.append((name_entry, x_entry, y_entry, delete_button))

    def delete_entry_row(self, row):
        for entry in self.entries[row-1]:
            entry.grid_forget()
        self.entries.pop(row-1)
        self.update_rows()

    def update_rows(self):
        for i, (name_entry, x_entry, y_entry, delete_button) in enumerate(self.entries):
            name_entry.grid(row=i+1, column=0, padx=5, pady=5)
            x_entry.grid(row=i+1, column=1, padx=5, pady=5)
            y_entry.grid(row=i+1, column=2, padx=5, pady=5)
            delete_button.grid(row=i+1, column=3, padx=5, pady=5)

    def plot_graph(self):
        data = [[], [], []]
        for name_entry, x_entry, y_entry, _ in self.entries:
            name = name_entry.get()
            try:
                x = float(x_entry.get())
                y = float(y_entry.get())
            except ValueError:
                messagebox.showerror("Eroare", "Valoarea x și valoarea y trebuie să fie numere.")
                return

            data[0].append(name)
            data[1].append(x)
            data[2].append(y)

        deseneaza_grafic(data)