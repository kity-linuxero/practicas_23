# Práctica 10 

## Programación orientada a Objetos - Parte II

En esta práctica nos concentraremos en consolidar los temas vistos en teorías, **clases**, **objetos**, **métodos**, **atributos**, **herencia**, **polimorfismo**, **encapsulación** y **abstracción** que son los conceptos básicos de la programación orientada a objetos.

También se introducirá el concepto de diagrama de clases UML.

## Introducción al diagrama de clases UML

Un programa informático tiene diversas formas de representarlos. Ver el código fuente y armar mentalmente las clases con la que está compuesto nuestro programa suele ser complicado cuando la solución es compleja.

Hasta el momento hemos visto soluciones muy simples con unas pocas clases, pero a continuación introduciremos un concepto para diagramar clases conocido como _Diagrama de clases UML_.

### Un ejemplo de diagrama de clases UML

En un diagrama de clase se puede especificar el nombre de la clase, sus atributos y, opcionalmente su tipo de datos, sus métodos con sus parámetros de entrada, opcionalmente el tipo de datos de retorno, la visibilidad de los métodos y atributos y la relación entre las clases.

![Una Clase](./img/pr10/clase_uml0.png)

En la visibilidad de datos, la notación es la siguiente:
- `+`: El atributo o método es __public__.
- `-`: El atributo o método es __private__.
- `#`: El atributo o método es __protected__.


En diagrama UML para representar una jerarquía de clase y subclases es la siguiente:

![Jerarquía de clases](./img/pr10/clase_uml1.png)

Donde se puede apreciar que `Subclase_1`y `Subclase_2` son clases _hijas_ de `Clase`. Y el atributo `atributo2` de `Clase` es _una instancia_ de `Otra_Clase`.

En caso de querer representar una [clase abstracta](https://programacion.concristian.com.ar/clase11-poo.html#/clase_abstracta) el título de la clase se pondrá en letra cursiva.

Los diagramas de clase suelen ser mucho mas complejos porque hay muchas variantes a tener en cuenta por ejemplo las relaciones entre clases. En las herencias aparecen nuevos conceptos como _generalización_ o _especialización_ que no son objeto de estudio en este curso.

[Diagramador online](https://app.diagrams.net/)

## Ejercicio 1

Crea una clase abstracta llamada `Figura_geometrica` con un método abstracto `calcular_area()`. Luego, crea subclases como `Rectangulo` y `Circulo` que hereden de esta clase y proporcionen implementaciones concretas de `calcular_area()`.



## Ejercicio 2
Realice un programa que contenga una _superclase_ `Animal` y luego una serie de _subclases_; `Gato`, `Perro`, `Pollo`, `Humano`.
Cada clase debe conocer los mensajes `hablar()` y `quien_sos()` y debe imprimir en pantalla un texto diferente como muestra la siguiente tabla

| Mensaje     	| Gato    	| Perro    	| Pollo    	| Humano    	|
|-------------	|---------	|----------	|----------	|-----------	|
| `hablar()`   	| Miau!   	| Guau!    	| Pio!     	| ¡Hola!    	|
| `quien_sos()`	| un Gato 	| un Perro 	| un Pollo 	| un Humano 	|

Para el mensaje `quien_sos()` utilice algún mecanismo que obtenga el nombre de la clase. No hagan _hardcoding_ del texto. :grin:

>**Hardcoding/hardcodear**: Es una mala práctica de programación. Consiste en incrustar datos directamente en el código fuente del programa, en lugar de obtener esos datos de una fuente externa. [Ref](https://es.wikipedia.org/wiki/Hard_code)



## Ejercicio 3
>Este ejercicio es una ampliación del [ejercicio 4](https://github.com/kity-linuxero/practicas_23/blob/main/practicas/practica9.md#ejercicio-5) de la práctica anterior.

Escriba un programa llamado `estructura_datos.py` y en él implemente utilizando _POO_ una estructura de datos **Pila** (si ya tiene hecho el ejercicio de la práctica anterior puede usarlo como guía) y otra estructura de datos **Cola**.

Ambas estructuras tienen similitudes y diferencias, mientras que una _Pila_ se trata de una estructura del tipo _LIFO_ (Last-In First-Out), es decir que el último en entrar es el primero en salir, la cola se basa en el tipo _FIFO_ (First-In First-Out), es decir que el primer elemento que ingresa es el primero en salir, como una cola de supermercado.

Las estructuras deben entender los siguientes mensajes:

#### Pila
- `apilar(elemento)`: Apila un elemento. Lo agrega en la estructura.
- `desapilar()`: Retorna el elemento de "más arriba" y lo quita de la pila.
- `top()`: Retorna el elemento de mas arriba pero no lo quita de la pila.
- `vacia()`: Retorna si la pila está vacía (`True`/`False`)
- `cant_elementos()`: Retorna _la cantidad_ de elementos que hay en la pila.

#### Cola
- `encolar(elemento)`: Encola un elemento. Lo agrega en la estructura.
- `desencolar()`: Retorna el primer elemento de la cola y lo quita de la misma.
- `top()`: Retorna el primer elemento pero no lo quita de la cola.
- `vacia()`: Retorna si la cola está vacía (`True`/`False`)
- `cant_elementos()`: Retorna _la cantidad_ de elementos que hay en la cola.

Como puede ver, hay mensajes que son los mismos y otros que varían un poco en su implementación. Utilice una superclase `Estructura_de_datos` y dos subclases `Pila` y `Cola` para implementar el código.
Puede apoyarse en una estructura `List` para ir almacenando los datos en las estructuras solicitadas.
Trate de reutilizar todo el código que pueda generalizando en la clase `Estructura_de_datos` el código que sea compartido.

>Importante: Respete el nombre de las clases; utilizando `Pila` para representar las pilas y `Cola` para representar las colas. Como también el nombre de los métodos propuestos. Puede crear métodos auxiliares si los necesita. Pero la interfaz hacia el usuario debe ser la sugerida.

## Ejercicio 4

Un banco tiene un sistema que ofrece _cajas de ahorro_ y _cuentas corrientes_. Ambas tienen un uso similar, pero la diferencia radica en que la cuenta corriente tiene un _monto al descubierto_ que por defecto será $10.000 por cuenta (el mismo puede ser cambiado solicitando al banco la ampliación del límite descubierto) lo que le permite extraer o transferir más dinero del que dispone en la cuenta.

Modele utilizando _POO_ la jerarquía de clases `Cuenta_bancaria` como _superclase_ y `Caja_ahorro` y `Cuenta_corriente` como _subclases_.

Las cuentas bancarias deben entender los siguientes mensajes:
- `saldo_disponible()`: Devuelve el saldo de la cuenta.
- `depositar(un_monto)`: Se hace un deposito en cuenta. Se debe incrementar el monto en la cuenta.
- `extraer(un_monto)`: Se realiza una extracción de dinero. Tener en cuenta el saldo descubierto de la cuenta corriente. Retorna True/False si se ha podido realizar la extracción o no respectivamente. Las cajas de ahorro tienen un límite de extracción diaria de $30.000 y las cuentas corrientes de $50.000. Puede solicitar al banco ampliar el límite.
- `transferir(cuenta_bancaria, un_monto)`: Transfiere a una cuenta bancaria enviada como parámetro el monto también enviado por parámetro. Las transferencias tienen una comisión del 0.9%. Las transferencias no tienen un límite en cuanto a monto.
- `modificar_limite_extracción(un_monto)`: Solicita al banco modificar el límite de extracción de dinero. Si el monto a solicitar es menor al limite actual, el banco lo acepta siempre. De lo contrario, será una opción random entre aceptarlo o no. La función debe retornar un True/False si el banco lo aceptó o no respectivamente.
- `modificar_limite_descubierto(un_monto)`: Aplica solo para las cuentas corrientes. Si el monto a solicitar es menor al descubierto actual, el banco lo acepta siempre. De lo contrario, será una opción random entre aceptarlo o no. La función debe retornar un True/False si el banco lo aceptó o no respectivamente.
- `limite_descubierto()`: Aplica solo para las cuentas corrientes. Devuelve el límite descubierto actual.
- `titular()`: Retorna el nombre del titular.
- `modificar_titular(nombre)`: Modifica el titular de la cuenta.

El siguiente diagrama de clases le puede ayudar a ver lo solicitado

![Diagrama de clases cuentas bancarias](./img/pr10/cuentas_bancarias.png)

Los tipos de datos que se hace referencia en el diagrama son:
- `float`: Tipo numérico flotante, es decir con decimales.
- `String`: Cadena de caracteres.
- `bool`: Tipo booleano (True/False).
- `void`: Se utiliza cuando no hay valor por retornar. Por lo que el método no retorna nada.

Tenga en cuenta la __protección de los atributos__ es decir, nadie debe poder modificar el atributo `monto` ni `titular` sin usar los métodos correspondientes.


# Ejercicios Extra

## Tarjeta SUBE

El Sistema Único de Boleto Electrónico, conocido como **SUBE**, es un servicio para pagar con una sola tarjeta viajes en colectivos, subtes y trenes. Tiene tarifa diferencial para jubilados, excombatientes, beneficiaros de planes y trabajadoras domésticas, como también beneficios como [_red sube_](https://www.argentina.gob.ar/redsube) que ofrece descuentos si se realizan una o más combinaciones en un lapso de 2 horas.

Realice un diagrama de clases que contenga la siguiente estructura.

- Sube
    - Normal
    - Diferencial (55% de descuento en los viajes)

La clase Sube

- `_titular`: Nombre y apellido del titular
- `_saldo`: El saldo en pesos de la tarjeta. El saldo descubierto (en negativo) deberá estar como variable de clase.
- `_id`: Es el número de la SUBE. Son 16 dígitos con el siguiente formato 6061 268x xxxx xxxx.
- `recargar(un_monto)`: Recarga la tarjeta con un monto
- `ultimo_viaje()`: Devuelve la hora del último viaje.
- `id`: Devuelve en formato legible el ID de la tarjeta.
- `titular`: Devuelve el nombre del titular
- `__str__()`: Devuelve el formato legible todos los datos de la SUBE. Por ejemplo:
```bash
    Titular: Juan Leiva
    Saldo: $ 134,56
    Número de tarjeta: 6061 2689 1323 1258
```
- `cobrar_viaje()`: Cobra un viaje.
    - Todos los viajes tendrán un valor fijado como variable de la clase Sube.
    - Depende el tipo de tarjeta se debe aplicar la tarifa correspondiente.
    - Tener en cuenta el beneficio de _red sube_:
        - Primer viaje: Se paga el total
        - Segundo viaje: Se paga el 50%
        - A partir del tercer viaje: se paga un 75% menos.
        - Los beneficios de la red sube aplica solo si en el lapso de dos horas se ha realizado el viaje. 
        
        Para simplificar, usaremos el lapso de 2 segundos para aplicar los descuentos de la red Sube y usaremos la sentencia `sleep()` para simular una demora.


El siguiente código es un ejemplo de un mensaje que se demora 5 segundos
```python
from time import sleep

print("Espero 5 segundos.")
sleep(5)
print("La espera ha terminado.")

```

> Recuerde que puede crear métodos y atributos auxiliares si los necesita.


Info sobre fechas y horas en Python: [link](https://oregoom.com/python/fechas-y-horas/)

Ref: [Sitio oficial Sube](https://www.argentina.gob.ar/sube)


-----



<img src="img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 90%">



