# El de las tablas de multiplicar
x = int(input("Ingrese un número "))

for j in range(1,11): # 10 repeticiones arrancando desde 1
    print(f"{x}*{j}= {x*j}")

j = 1
while (j <11): # Itera 10 veces
    print(f"{x}*{j}= {x*j}")
    j+=1
