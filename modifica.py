import os
from countdown import countdown

def modifica():
    try:
        Quale = input("\nInserisci la matricola da modificare: ").strip()
        countdown(5,2,"Controllo")
        trovata = False

        with open("file.txt", "r", encoding="utf-8") as file, open("fil.txt", "w", encoding="utf-8") as temp_file:
           
            for riga in file:
                solo = "".join(c for c in riga if c.isdigit())
                if solo == Quale:
                    trovata = True
                    cambionome = input("\nInserisci il nuovo nome: ")
                    countdown(3,2,"Modifico")
                    cambicognome = input("\nInserisci il nuovo cognome: ")
                    countdown(3,2,"Modifico")
                    temp_file.write(f"| {Quale:<9} | {cambicognome.capitalize():<8} | {cambionome.capitalize():<9} |\n")
                    continue
                temp_file.write(riga)


        os.remove("file.txt")
        os.rename("fil.txt", "file.txt")
        countdown(3,2,"Eseguo il salvataggio")
        print("Modifica completata con successo.")
        
        if not trovata:
            print("Matricola non trovata.")
            return


    except FileNotFoundError:
        print("Il file 'file.txt' non esiste.")

    except Exception as e:
        print(f"Errore Improvviso!!! {e}")
    
