from time import sleep
import time


class Sube:
        
    tarifa_viaje = 50  # Tarifa predeterminada por viaje
    tiempo_para_descuento = 2  # 2 segundos para aplicar descuento
    saldo_descubierto_maximo=-100

    def __init__(self,titular):
        self._titular=titular
        self._saldo=0
        self._id = self.generador_de_ID()
        self._ultimo_viaje=0 #guion agregado para que no de error, pero en realida deberia ser sin y llamar al metodo de mismo nombre, da  TypeError: 'int' object is not callable

    def recargar(self,monto):
        if monto>=0:
            self._saldo+=monto
            print("la carga de saldo fue procesada con exito")
        else:
            print("el monto ingresado es erroneo")
    def generador_de_ID(self):
        import random
        numeros="1","2","3","4","5","6","7","8","9","0"
        id_temp = "6061268"
        for e in range(9):
            id_temp+=random.choice(numeros)  #genera los numeros faltantes del id, pero todos juntos
        id = f"{id_temp[0:4]} {id_temp[4:8]} {id_temp[8:12]} {id_temp[12:19]}" #se encarga de separar de 4 en 4 los digitos del serial
        #print(id)
        return id
  

    def consultar_saldo(self):
        print("el saldo disponible es de: $",self._saldo)
    def ultimo_viaje(self):
        self.tiempo_ultimo_viaje
        return self.tiempo_ultimo_viaje
    def descuento(self):
        #tiempo_para_descuento=7200
        if  self.ultimo_viaje() <=(self.tiempo_para_descuento):#compara la hora del ultimo viaje con la hora actual - 7200 seg (2hs)
           # self._saldo+=self.tarifa_viaje%2 
            print("descuento procesado")
            return True
      
    def titular(self,titular):
        self.titular=titular
        pass
    def cobrar_viaje(self):
        hora=time.time()
        self.tiempo_ultimo_viaje=hora

        if self.descuento()==False:
            tarifa_viaje=50
            print("se ha cobrado un voleto estandar")
        else:
            tarifa_viaje=25
            print("se ha cobrado un volento con descuento")
        self._saldo-=tarifa_viaje
        print(f"pago exitoso: ${tarifa_viaje} El saldo restante es de: ${self._saldo}")
class Normal(Sube):    
    def __init__(self, titular):
        super().__init__(titular) 
    def cobrar_viaje(self):
        hora=time.time()
        self.tiempo_ultimo_viaje=hora

        if self.descuento()==False:
            tarifa_viaje=50
            print("se ha cobrado un voleto estandar")
        else:
            tarifa_viaje=25
            print("se ha cobrado un volento con descuento")
        self._saldo-=tarifa_viaje
        print(f"pago exitoso: ${tarifa_viaje} El saldo restante es de: ${self._saldo}")
           
class Diferencial(Sube):
    def __init__(self, titular):
        super().__init__(titular)
    def cobrar_viaje(self):
        hora=time.time()
        self.tiempo_ultimo_viaje=hora

        if self.descuento()==False:
            tarifa_viaje=50
            print("se ha cobrado un voleto estandar")
        else:
            tarifa_viaje=25
            print("se ha cobrado un volento con descuento")
        self._saldo-=tarifa_viaje
        print(f"pago exitoso: ${tarifa_viaje} El saldo restante es de: ${self._saldo}")


#'''
if __name__ == '__main__':

    sube1=Sube("Agustin Giugovaz")
    sube1.generador_de_ID()
    sube1.cobrar_viaje()
    sube1.consultar_saldo()
    sube1.recargar(200)
    sube1.consultar_saldo()
    #sube1.ultimo_viaje()
    sleep(5)
    sube1.cobrar_viaje()
# sube1.descuento()
   
    sube2=Sube("feernando perez")
    sube2.generador_de_ID()

    sube2.recargar(100)
    sube2.consultar_saldo()
    sube2.cobrar_viaje()
    sube2.descuento()    # '''