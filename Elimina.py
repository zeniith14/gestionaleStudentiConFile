import os
from countdown import countdown

def elimina():
    try:
        matricola = input("\nInserisci la matricola da eliminare: ").strip()
        countdown(2, 2, "Cerco")

        # Chiedo conferma finché non è valida
        while True:
            sicuro = input(f"\nSei sicuro di voler ELIMINARE questa matricola [{matricola}]? Y/N: ").strip().lower()
            if sicuro in ("y", "n"):
                break
            print("Digita Y o N")

        # Se annulla, esco senza toccare i file
        if sicuro == "n":
            countdown(2, 2, "Annullo")
            return

        # Se conferma, creo il file temporaneo filtrato
        trovata = False
        with open("file.txt", "r", encoding="utf-8") as file, open("fil.txt", "w", encoding="utf-8") as fil:
            for riga in file:
                solo = "".join(ch for ch in riga if ch.isdigit())
                if solo == matricola:
                    trovata = True
                    continue
                fil.write(riga)

        if not trovata:
            print("Matricola non trovata. Nessuna modifica.")
            os.remove("fil.txt")
            return

        # Sostituzione sicura
        os.remove("file.txt")
        os.rename("fil.txt", "file.txt")
        print("Eliminazione completata.")

    except FileNotFoundError:
        print("Il file 'file.txt' non esiste.")
    except Exception as e:
        print(f"Errore improvviso: {e}")
