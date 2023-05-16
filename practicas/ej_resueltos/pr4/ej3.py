from random import randint

dado = ['1','2','3','4','5','6']
while True:
    us = input("Elija un número del 1 al 6: ")
    if us in dado:
        print("Se lanza el dado...")
        pc = randint(1,6)
        print(f"Salió el número {pc}")

        if int(us) != pc:
            print("No acertaste")
        else:
            print("¡Ganaste!")
            break