import random
import os
from countdown import countdown

def matricola(lunghezza=5):
    return "".join(str(random.randint(0, 9)) for _ in range(lunghezza))

def aggiungi():
    try:
        print("\nAggiungiamo Studente")
        nome = input("\nInserisci il nome dello studente: ").strip()
        countdown(2, 2, "Salvo")
        cognome = input("\nInserisci il cognome dello studente: ").strip()
        countdown(2, 2, "Salvo")

        m = matricola()

        # scrivo su file in formato tabella markdown
        file_esiste = os.path.exists("file.txt")
        file_vuoto = (not file_esiste) or os.stat("file.txt").st_size == 0

        with open("file.txt", "a", encoding="utf-8") as file:
            if file_vuoto:
                file.write("| Matricola | Cognome  | Nome      |\n")
                file.write("| --------- | -------- | --------- |\n")

            # larghezze per allineamento
            file.write(f"| {m:<9} | {cognome.capitalize():<8} | {nome.capitalize():<9} |\n")

        print(f"\nLa matricola di {nome} {cognome} è {m}")

        menu_aggiungi()

    except Exception as e:
        print(f"Errore Improvviso!!! {e}")

def menu_aggiungi():
    while True:
        scelta = input("\nVuoi continuare? Y o N: ").strip().lower()
        if scelta == "y":
            aggiungi()
            return
        elif scelta == "n":
            print("Okay")
            return
        else:
            print("Inserisci una risposta valida (Y/N)")
