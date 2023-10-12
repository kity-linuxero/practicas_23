import time
import random

class Sube:
    saldo_descubierto_maximo = -100  # Saldo máximo negativo permitido
    tarifa_viaje = 50  # Tarifa predeterminada por viaje
    tiempo_para_descuento = 1  # 1 segundos para aplicar descuento
    NORMAL = 1
    RED_SUBE = 0.50

    def __init__(self, titular):
        self._titular = titular
        self._saldo = 0.0
        self._id = self.generar_id()
        self._ultimo_viaje = 0

    def generar_id(self):
        # Genera un número de SUBE aleatorio para simular la creación de un ID
        id = "6061 268" + str(random.randint(0, 9)) + " " + str(random.randint(1000, 9999)) + " " + str(random.randint(1000, 9999))
        return id

    def recargar(self, un_monto):
        try:
            if un_monto <= 0:
                print("La recarga debe ser un valor válido")
                return False
            self._saldo += un_monto
            print(f"Recarga exitosa. Nuevo saldo: {self._saldo}")
            return True
        except:
            return False


    def ultimo_viaje(self):
        if self._ultimo_viaje:
            return self._ultimo_viaje
        return "Ningún viaje registrado."

    def id(self):
        return self._id

    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    def cumple_red_sube(self, hora):
        return hora-self._ultimo_viaje <= self.tiempo_para_descuento
    
    def __cobrar_viaje(self, costo, hora):
        self._saldo -= costo
        self._ultimo_viaje = hora

    def __calcular_costo_viaje(self, descuento, hora):
        # Verifico si aplica el descuento adicional por red sube
        descuento_red_sube = self.NORMAL if not self.cumple_red_sube(hora) else self.RED_SUBE
        # Calculo el valor del viaje
        return self.tarifa_viaje * descuento * descuento_red_sube

    def cobrar_viaje(self, descuento=1):
        # Registro el horario
        hora = time.time()
        
        costo_viaje = self.__calcular_costo_viaje(descuento,hora)
        
        if self._saldo + abs(self.saldo_descubierto_maximo) < costo_viaje:
            print("Saldo insuficiente para viajar.")
            return False
        
        else: # Hay saldo
            self.__cobrar_viaje(costo_viaje, hora)
            print(f"Viaje exitoso. Nuevo saldo: {self._saldo}")
            return True

class Normal(Sube):
    pass

class Diferencial(Sube):

    def cobrar_viaje(self):
        return super().cobrar_viaje(0.45)
