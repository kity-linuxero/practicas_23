# Pruebas unitarias
import unittest
from sube import *

class TestSube(unittest.TestCase):

    TIME_DELTA = 0.1 # Retraso para no cobrar el beneficio de Red Sube

    def setUp(self):
        self.sube_normal = Normal("Juan Perez")
        self.sube_diferencial = Diferencial("Maria Lopez")

    def test_id_sube(self):
        """
        Se utiliza una expresión regular (regex) para validar el número de la Sube. Mas info en:
        
        https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular

        https://www.w3schools.com/python/python_regex.asp
        """

        import re

        
        patron = r'^6061 268\d{1} \d{4} \d{4}$'

        self.assertTrue(re.match(patron, self.sube_normal._id), f"El formato del id {self.sube_normal._id} NO es válido")

    def test_recargar(self):
        self.assertTrue(self.sube_normal.recargar(50))
        self.assertFalse(self.sube_normal.recargar('a'))
        self.assertFalse(self.sube_normal.recargar(-20))

        self.assertTrue(self.sube_diferencial.recargar(50))
        self.assertFalse(self.sube_diferencial.recargar('a'))
        self.assertFalse(self.sube_diferencial.recargar(-20))

        
    def test_cobrar_viaje_sube_normal(self):

        Sube.saldo_descubierto_maximo = -50
        Sube.tiempo_para_descuento = 0.2

        self.sube_normal.recargar(50)
        
        # Test cobra un pasaje. Debe quedar en 0
        self.assertTrue(self.sube_normal.cobrar_viaje())
        self.assertEqual(0.0,self.sube_normal.saldo)
        
        # Espera mas del tiempo para que cobre completo
        time.sleep(Sube.tiempo_para_descuento+self.TIME_DELTA)

        # Test cobra un pasaje. Debe quedar en -50.0
        self.assertTrue(self.sube_normal.cobrar_viaje())
        self.assertEqual(-50.0,self.sube_normal.saldo)
        
        # Ya no se puede viajar
        self.assertFalse(self.sube_normal.cobrar_viaje())
        self.assertEqual(-50.0,self.sube_normal.saldo)

    
    def test_cobrar_viaje_sube_diferencial(self):

        Sube.saldo_descubierto_maximo = -25
        Sube.tiempo_para_descuento = 0.2

        self.sube_diferencial.recargar(20)
        
        # Test cobra un pasaje. Debe quedar en -2,50
        self.assertTrue(self.sube_diferencial.cobrar_viaje())
        self.assertEqual(-2.5,self.sube_diferencial.saldo)
        
        # Espera mas del tiempo para que cobre completo
        time.sleep(Sube.tiempo_para_descuento+self.TIME_DELTA)

        # Test cobra un pasaje. Debe quedar en -25
        self.assertTrue(self.sube_diferencial.cobrar_viaje())
        self.assertEqual(-25.0,self.sube_diferencial.saldo)
        
        # Ya no se puede viajar
        self.assertFalse(self.sube_diferencial.cobrar_viaje())
        self.assertEqual(-25.0,self.sube_diferencial.saldo)

    
    def test_red_sube_normal(self):
        Sube.saldo_descubierto_maximo = -25
        Sube.tiempo_para_descuento = 0.2

        tarifa = Sube.tarifa_viaje

        # Primer viaje
        self.sube_normal.recargar(100)
        self.sube_normal.cobrar_viaje()

        # Segundo viaje en combinación. Se aplica el descuento
        saldo = self.sube_normal.saldo
        self.sube_normal.cobrar_viaje()
        self.assertEqual(self.sube_normal.saldo,(saldo - tarifa*0.5),"No se aplicó correctamente el descuento de Red Sube del -50%")


    def test_red_sube_diferencial(self):
        
        Sube.saldo_descubierto_maximo = -25
        Sube.tiempo_para_descuento = 0.2

        tarifa = Sube.tarifa_viaje * 0.45

        # Primer viaje
        self.sube_diferencial.recargar(100)
        print(f"Hola {self.sube_diferencial.saldo}")
        self.sube_diferencial.cobrar_viaje()

        # Segundo viaje en combinación. Se aplica el descuento
        saldo = self.sube_diferencial.saldo
        self.sube_diferencial.cobrar_viaje()
        self.assertEqual(self.sube_diferencial.saldo,(saldo - tarifa*0.5),"No se aplicó correctamente el descuento de Red Sube del -50%")


if __name__ == '__main__':
    unittest.main()
