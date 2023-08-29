class Auto:

    MANTENIMIENTO=10000

    def __init__(self, modelo):
        self.modelo = modelo 
        self.km = 0
        self.mant = self.MANTENIMIENTO 

    def recorrido(self, km):
        self.km += abs(km)
        if self.km >= self.mant:
            print("Es necesario realizar el mantenimiento")
        
    def kilometraje(self):
        print(self.km)

    def realizar_mantenimiento(self):
        self.mant = self.km+self.MANTENIMIENTO
        print("Se ha realizado el mantenimiento")


a = Auto('Focus')

a.recorrido(9000)
a.kilometraje()
a.recorrido(6000)
a.realizar_mantenimiento()
a.recorrido(500)
a.recorrido(1500)
a.kilometraje()
print(a.mant)


    





    

