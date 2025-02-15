from graph import creeaza_date, deseneaza_grafic

if __name__ == "__main__":
    file_path = 'data.csv'
    date = creeaza_date(file_path)
    deseneaza_grafic(date)
