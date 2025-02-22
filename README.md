# Aplicație Python pentru Vizualizarea Interactivă a Datelor

Acest proiect Python permite vizualizarea datelor pe un grafic 2D, conectarea punctelor cu o linie discontinuă și afișarea numelui asociat fiecărui punct. Este folosită librăria `matplotlib` pentru a crea graficele și `numpy` pentru a manipula datele.

## Utilizare GUI

Pentru a rula programul și a vizualiza graficul folosind interfața grafică:

1. Execută scriptul Python `main.py`:
    ```sh
    python main.py
    ```

2. În fereastra GUI, poți adăuga rânduri de date introducând numele, valoarea x și valoarea y în câmpurile corespunzătoare și apăsând butonul "Adaugă rând".

3. Pentru a șterge un rând, apasă butonul "Șterge" de lângă rândul pe care dorești să-l elimini.

4. După ce ai introdus toate datele, apasă butonul "Desenează grafic" pentru a genera și vizualiza graficul.

## Structura Proiectului

- `main.py`: Scriptul principal care lansează interfața grafică.
- `gui.py`: Conține clasa `DataEntryApp` care gestionează interfața grafică pentru introducerea datelor.
- `graph.py`: Conține funcțiile pentru citirea datelor din fișierul CSV și desenarea graficului.
- `data.csv`: Fișierul CSV cu datele de intrare.

## Dependențe

Asigură-te că ai instalat următoarele pachete Python:

- `tkinter`
- `matplotlib`
- `numpy`

Le poți instala folosind `pip`:

```sh
pip install matplotlib numpy tkinter
```

## Funcționalități
- Adăugare Rânduri: Permite adăugarea de noi rânduri de date în interfața grafică.
- Ștergere Rânduri: Permite ștergerea rândurilor de date din interfața grafică.
- Desenare Grafic: Generează și afișează un grafic 2D pe baza datelor introduse sau încărcate din fișierul CSV.
- Sortare Date: Sortează datele pe baza valorilor x înainte de a le afișa pe grafic.
- Etichetare Puncte: Afișează numele asociat fiecărui punct pe grafic.