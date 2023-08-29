class Persona:    
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Método saludar
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

lista = []
# main
while (True):
    n = input("Ingrese nombre: ")
    if n == '@fin':
        break
    e = input("Su edad: ")
    p = Persona(n,e)
    lista.append(p)

for n in lista:
    n.saludar()

print(lista)
