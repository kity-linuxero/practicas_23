import time


class Sube:

    saldo_descubierto_maximo = -100
    # Saldo máximo negativo permitido
    tarifa_viaje = 50  # Tarifa predeterminada por viaje

    tiempo_para_descuento = 2

    def __init__(self, un_nombre):
        self.nombre = un_nombre
        self.saldo = 0
        self._id = self.id()
        self.ultimo_viaje_tiempo = 0

    def titular(self):

        return self.nombre

    # Recarga la tarjeta con un monto. Debe regresar:
    def recargar(self, un_monto):
        try:
            if un_monto < 0:
                # Falseen caso que se ingrese un valor imposible o menor/igual a 0.
                return False
            else:                    # Trueen caso que la carga se haga exitosa.
                self.saldo += un_monto
                return True
        except TypeError:
            print("Debe ingresar un numero para recargar")
            return False

    def id(self):  # genera el id de la targeta
        import random
        id = "6061 268"
        ok = 3
        for i in range(9):
            new = random.randrange(0, 10)
            id += str(new)
            if ok == 3:
                id += " "
                ok = 0
            else:
                ok += 1
                self._id = id

        return id.strip()

    def cobrar_viaje(self):

        tiempo_viaje = time.time()

        if tiempo_viaje - self.ultimo_viaje_tiempo <= self.tiempo_para_descuento:  # descuento el tiempo
            self.ultimo_viaje_tiempo = tiempo_viaje
            return self.calcular_tarifa(0.5)

        else:
            self.ultimo_viaje_tiempo = tiempo_viaje
            return self.calcular_tarifa(1.0)

    def calcular_tarifa(self, porc_a_cobrar):

        if self.saldo >= self.tarifa_viaje * porc_a_cobrar or self.saldo_descubierto_maximo + self.saldo <= self.tarifa_viaje * porc_a_cobrar and self.saldo_descubierto_maximo + self.saldo >= self.saldo_descubierto_maximo:
            self.saldo -= self.tarifa_viaje * porc_a_cobrar
            return True
        else:
            return False

    def ultimo_viaje(self):
        if self.ultimo_viaje_tiempo == 0:
            return "Ningún viaje registrado"
        else:
            return f"Último viaje registrado {time.ctime((self.ultimo_viaje_tiempo))}"


class Normal(Sube):
    pass


class Diferencial(Sube):

    def calcular_tarifa(self, porc_a_cobrar):

        # le multiplico 0.45 para que cobre el 55% (En el 2 viaje se aplica el descuento? del 50?
        porc_a_cobrar = porc_a_cobrar * 0.45

        if self.saldo >= self.tarifa_viaje * porc_a_cobrar or self.saldo_descubierto_maximo + self.saldo <= self.tarifa_viaje * porc_a_cobrar and self.saldo_descubierto_maximo + self.saldo >= self.saldo_descubierto_maximo:
            self.saldo -= self.tarifa_viaje * porc_a_cobrar
            return True
        else:
            return False


# main
if __name__ == "__main__":
    sube_normal = Normal("Juan Perez")
    sube_diferencial = Diferencial("Maria Lopez")

    print(sube_diferencial.nombre)
    print(sube_diferencial.recargar(50))
   # print(sube_diferencial.recargar("a"))
    print(sube_diferencial.cobrar_viaje())
    print(sube_diferencial.saldo)
    print(sube_diferencial.cobrar_viaje())

    print(sube_diferencial.cobrar_viaje())

    print(sube_diferencial.cobrar_viaje())

    print(sube_diferencial.cobrar_viaje())

    print(sube_diferencial.cobrar_viaje())
    print(sube_diferencial.cobrar_viaje())
    print(sube_diferencial.cobrar_viaje())
    print(sube_diferencial.cobrar_viaje())

    print(sube_diferencial.saldo)
    print(sube_diferencial.ultimo_viaje())
