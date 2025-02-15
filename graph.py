import matplotlib.pyplot as plt
import csv

def creeaza_date(file_path):
    date = []
    with open(file_path, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            for i, value in enumerate(row):
                if len(date) <= i:
                    date.append([])
                try:
                    date[i].append(float(value) if i > 0 else value)
                except ValueError:
                    date[i].append(value)
    return date

def deseneaza_grafic(date):
    nume, valori_x, valori_y = date

    # Sortarea datelor pe baza valorilor x
    date_sortate = sorted(zip(valori_x, valori_y, nume))
    valori_x_sortate, valori_y_sortate, nume_sortate = zip(*date_sortate)

    # Plasarea punctelor sortate pe grafic cu etichete
    plt.scatter(valori_x_sortate, valori_y_sortate, color='b', label='Puncte de date')

    # Conectarea punctelor sortate cu o linie discontinuă
    plt.plot(valori_x_sortate, valori_y_sortate, linestyle='dashed', color='r', label='Conexiune')

    # Adăugarea etichetelor pentru fiecare punct
    for i, nume in enumerate(nume_sortate):
        plt.text(valori_x_sortate[i], valori_y_sortate[i], nume, fontsize=12, ha='right', rotation=25)

    # Setarea etichetelor și titlului
    plt.xlabel('Valoare x')
    plt.ylabel('Valoare y')
    plt.title('Grafic x si y', fontsize=20)
    plt.grid(True)

    plt.tight_layout()
    plt.show()