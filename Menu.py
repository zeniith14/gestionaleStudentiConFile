
from Aggiungi import aggiungi
from Elimina import elimina
from modifica import modifica
from countdown import countdown



def menu():
   

    while True:
        print("1 = Aggiungi \n2 = Modifica \n3 = Elimina dati \n4 = Esci")
        try:

            scelta = int(input("Inserisci un numero: "))
            
            if scelta == 1:
                countdown(5,2,"Trasferisco")
                aggiungi()

            elif scelta == 2:
                countdown(5,2,"Trasferisco")
                modifica()

            elif scelta == 3:
                countdown(5,2,"Trasferisco")
                elimina()

            elif scelta == 4:
                print("Uscita in corso...")
                countdown(3,1,"chiuso")
                break   
            else:
                print("Inserisci un numero valido")

            
            
        except ValueError:
            print("Inserisci solo numeri")



