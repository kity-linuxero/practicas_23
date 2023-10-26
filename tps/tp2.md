# Trabajo práctico N°2

El siguiente TP es para la evaluación de los conceptos de Orientación a objetos y se solicita que se realice una modificación del último ejercicio de la práctica 10.
Se debe realizar el diseño de las clases y atributos y métodos.

Importante: Respetar el nombre de los métodos y atributos sugeridos.

Fecha de entrega: 13/10/2023



## Tarjeta SUBE

El Sistema Único de Boleto Electrónico, conocido como **SUBE**, es un servicio para pagar con una sola tarjeta viajes en colectivos, subtes y trenes. Tiene tarifa diferencial para jubilados, excombatientes, beneficiaros de planes y trabajadoras domésticas, como también beneficios como [_red sube_](https://www.argentina.gob.ar/redsube) que ofrece descuentos si se realizan una o más combinaciones en un lapso de 2 horas.

Realice un programa que contenga la estructura de clases siguiente:

- Sube
    - Normal
    - Diferencial (55% de descuento en los viajes)


##### La clase Sube

- `_titular`: Nombre y apellido del titular
- `_saldo`: El saldo en pesos de la tarjeta.
- `_id`: Es el número de la SUBE. Son 16 dígitos con el siguiente formato 6061 268x xxxx xxxx.
- `recargar(un_monto)`: Recarga la tarjeta con un monto. Debe retornar:
    - `False` en caso que se ingrese un valor imposible o menor/igual a 0.
    - `True` en caso que la carga se haga exitosa. 
- `ultimo_viaje()`: Retorna:
    - _Ningún viaje registrado._ Si no se ha registrado ningún viaje. (Un string)
    - Si se ha realizado un viaje retorna la hora registrada.
- `id`: Devuelve en formato legible el ID de la tarjeta, por ejemplo `6061 2689 1323 1258`. El formato debe ser un string.
- `titular`: Devuelve el nombre del titular

- `cobrar_viaje()`: Cobra un viaje.
    - Depende el tipo de tarjeta se debe aplicar la tarifa correspondiente.
    - Tener en cuenta el beneficio de _red sube_:
        - Primer viaje: Se paga el total
        - Segundo viaje: Se paga el 50%
        - ~~A partir del tercer viaje: se paga un 75% menos~~ 
    
    Los beneficios de la red sube aplica solo han pasado menos de dos horas del último viaje.
        
    Para simular la demora usaremos `sleep` de `time`. Y usaremos la variable de clase `tiempo_para_descuento` para definir el tiempo expresado en segundos para calcular el descuento de la red sube.

El siguiente código es un ejemplo de un mensaje que se demora 5 segundos
```python
from time import sleep

print("Espero 5 segundos.")
sleep(5)
print("La espera ha terminado.")

```

**Getter y setters**: Encapsule el atributo y escriba un getter para obtener el dato, por ejemplo:

```python

class Prueba:
    
    def __init__(self, nombre):
        self._nombre = nombre
    
    # getter
    def nombre(self):
        return self._nombre

```

Utilice las siguientes variables de clase para tener los valores:

```python
class Sube:
    saldo_descubierto_maximo = -100  # Saldo máximo negativo permitido
    tarifa_viaje = 50  # Tarifa predeterminada por viaje
    tiempo_para_descuento = 2  # 2 segundos para aplicar descuento

```

#### Marca de hora

Para definir el tiempo o marca de tiempo, algo que se suele usar es el tiempo desde el _epoch_. Es decir, la cantidad de tiempo que pasó desde el 1 de enero de 1970 00:00:00 UTC, dicho tiempo se lo conoce como `timestamp` o `Unix Time` [ref](https://es.wikipedia.org/wiki/Tiempo_Unix).

De esa manera podemos usar el paso del tiempo de una manera sencilla.
Por ejemplo: 

```python
import time
hora = time.time()
print(hora)
```

#### El resultado será:

```bash
1694658895.68325
```
Eso es el tiempo, expresado en segundos, que pasó desde el epoch.

Con ese número podemos calcular hasta la fracción de segundo en qué momento ocurrió un evento.

Mas info: [Python time (en inglés)](https://www.programiz.com/python-programming/time)

## Importante

El programa debe pasar los [test de unidad](https://github.com/kity-linuxero/practicas_23/blob/main/tps/tp2-files/test_sube.py) propuestos


### Referencias
- [Python time (en inglés)](https://www.programiz.com/python-programming/time)
- Info sobre fechas y horas en Python: [link](https://oregoom.com/python/fechas-y-horas/)
- [Sitio oficial Sube](https://www.argentina.gob.ar/sube)


-----

<img src="../practicas/img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 40%">


