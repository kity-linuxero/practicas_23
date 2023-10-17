#TP2
import time

class Sube():
    saldo_descubierto_maximo = -100  # Saldo máximo negativo permitido
    tarifa_viaje = 50  # Tarifa predeterminada por viaje
    tiempo_para_descuento = 2  # 2 segundos para aplicar descuento
    hora=0
    def __init__(self, titular):
        self.titular=titular
        self.saldo=0
        self._id= self.id()
        self.viajes=0
    def recargar(self, un_monto):
        #self.saldo = self.saldo + un_monto
        try:
            if un_monto > 0:
                self.saldo += un_monto
                return True
        except TypeError:
            return False
        else:
            return False
    def ultimo_viaje(self):
        if self.viajes > 0:
            return self.viajes
        else:
            print("Ningún viaje registrado.")
    def id(self):
        import random
        id = "6061 268"
        randomNumber = random.randint(0,9)
        id+=str(randomNumber)+' '
        randomNumber = random.randint(1000,9999)
        id+=str(randomNumber)+' '
        randomNumber = random.randint(1000,9999)
        id+=str(randomNumber)
        return id
    def titular():
        pass
    def __str__(self):
        return (f" Titular: {self.titular}\n id: {self._id}\n Saldo: {self.saldo}\n Ultimo viaje:  {self.viajes}")
    
    def cobrar_viaje(self, descuento):
        #Primer viaje: Se paga el total
        #Segundo viaje: Se paga el 50%
        
        hora_viaje = time.time()
        descuento_red_sube = self.aplicar_descuento(hora_viaje)

        if self.tarifa_viaje * descuento * descuento_red_sube <= self.saldo - self.saldo_descubierto_maximo: 
            self.saldo -= self.tarifa_viaje * descuento * descuento_red_sube
            self.viajes = hora_viaje
            return True        
        else:
            print("Fondo insuficiente")
            return False
    
    def aplicar_descuento(self, hora_viaje):
        if (hora_viaje - self.viajes) < self.tiempo_para_descuento:
            return 0.5
        else:
            return 1
        

class Normal(Sube):
    def __init__(self, titular):
        super().__init__(titular)
    def cobrar_viaje(self):
        return super().cobrar_viaje(1)
class Diferencial(Sube):#55% de descuento en los viajes
    def __init__(self, titular):
        super().__init__(titular)
    def cobrar_viaje(self):
        return super().cobrar_viaje(0.45)


#main
if __name__ == '__main__':
    s=Normal("Juan")
    s.recargar(100)
    print(s)
    s.cobrar_viaje()
    print(s)
    s.cobrar_viaje()
    print(s)
    time.sleep(3)
    s.cobrar_viaje()
    print(s)
    s.cobrar_viaje()
    print(s)
    s.cobrar_viaje()
    print(s)

    #d=Diferencial("Pedro")
    #d.recargar(100)
    #d.cobrar_viaje()
    #print(d)