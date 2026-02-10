import time

def countdown(seconds , quale, scrittura):
    if quale == 1:
        print("Sto eseguendo la chiusura")
        for i in range(seconds, 0, -1):
            print(i)
            time.sleep(1)
        print(scrittura)
    if quale == 2:
        print(scrittura, end="")
        for i in range(seconds, 0, -1):
            time.sleep(0.5)
            print(".", end="", flush=True)


