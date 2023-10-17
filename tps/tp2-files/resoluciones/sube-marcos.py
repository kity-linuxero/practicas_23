import time
import random

class Sube:
    saldo_descubierto_maximo = -100
    tarifa_viaje = 50
    tiempo_para_descuento = 2

    def __init__(self,nombre):
        self._usuario=nombre
        self._saldo=0
        self._idnum=self.generador_id()
        self._registro_viaje="No hubo viajes."

    def generador_id(self):
        ejemplo="6061 268x xxxx xxxx"
        valor=''
        for i in ejemplo:#itera por cada caracter y si es una x lo cambia por un numero random
            if i=="x":
                i=random.randint(0,9)
            valor+=str(i)

        return valor

    def recargar(self,un_monto):#false si es invalida ,true si es exitosa
        valor=False
        try:
            print(f"\nUsted intentó recargar:{un_monto}")
            un_monto=int(un_monto)
            if 0<un_monto:
                self._saldo+=un_monto
                valor=True
                print("Recarga valida.")
            else:
                print(f"{un_monto} no es un monto valido.")
        except ValueError:
            print("Valor de recarga no valido.")
        return valor

    def ultimo_viaje(self):#return"no hubo viaje" o return hora del ultimo viaje
        return self._registro_viaje
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,valor_test):
        self._saldo=valor_test

    @property
    def _id(self):
        return self._idnum
    
    @property
    def _titular(self):
        return self._usuario
    
    def red_sube(self):#calcula si el tiempo entre viajes es valido para aplicar descuento RedSube
        if self._registro_viaje!="No hubo viajes.":
            hora_actual=time.time()
            hora_ultimo=self._registro_viaje
            valor=hora_actual-hora_ultimo
            if valor<self.tiempo_para_descuento:
                valor=True
            else:
                valor=False
        else:
            valor=False
        return valor
    
    def calculo_de_descunto(self,tarifa_actual):#aplica el descuento de subsidio,0% para normal y 55% para diferencial
        tarifa=tarifa_actual-(tarifa_actual*self.descuento)/100
        return tarifa
    
    def cobrar_viaje(self):
        tarifa_viaje_actual=self.tarifa_viaje
        descuento_redsube=self.red_sube()#True si el tiempo es valido False si el tiempo se pasó
        if descuento_redsube==True:
            tarifa_viaje_actual=tarifa_viaje_actual-(tarifa_viaje_actual)/2.0#aplica el descuento de 50%
            

        tarifa_con_descuento=self.calculo_de_descunto(tarifa_viaje_actual)
        saldo_final = self._saldo - tarifa_con_descuento
        if self.saldo_descubierto_maximo<=saldo_final:#calcula si el saldo despues de pagar es mayor que el limite de la tarjeta
            self._saldo = self._saldo - tarifa_con_descuento
            self._registro_viaje = time.time()
            valor=True
            print(f"\nSaldo restante: ${self.saldo}")
        else:
            valor=False
            print(f"\nSaldo insuficiente : {self.saldo}")
        return valor
    

class Normal(Sube):
    descuento=0
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def recargar(self, un_monto):
        return super().recargar(un_monto)
    
    def cobrar_viaje(self):
        return super().cobrar_viaje()
       
class Diferencial(Sube):
    descuento=55

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def recargar(self, un_monto):
        return super().recargar(un_monto)
    def cobrar_viaje(self):
        return super().cobrar_viaje()
