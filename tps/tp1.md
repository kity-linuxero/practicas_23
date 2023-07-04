# Trabajo práctico N°1

## Diccionario de palabras

Hoy en día es muy común que los editores de textos medianamente sofisticados tengan la característica de poder verificar ortografía, palabras y formas de redacción.

Con los conocimientos adquiridos en este curso, estamos en condiciones para poder hacer una comprobación simple de palabras en una cadena de caracteres o archivo y comprobarlos si están bien escritas. Esto le ayudará a reafirmar sus habilidades para programar y resolver problemas.


## Programa a desarrollar

Desarrolle un programa que permita verificar si las palabras escritas en una sucesión de palabras se encuentran en un diccionario provisto de palabras en español.

[Descargar el diccionario](https://programacion.concristian.com.ar/img/spanish.zip)

### Primera etapa

Desarrolle un programa que permita que el usuario escriba texto _en modo interactivo_ hasta que llegue la palabra `@fin`. En dicho momento debe terminar la toma de palabras y debe informar la cantidad de palabras escritas que no figuran en el diccionario.

```
¡Bienvenido al TP1 del curso de programación!
Usted ha ingresado al modo interactivo.

> Hola, esto es un texto de prueba.
> Texto, texto y mas texto... kljakljdja fasdfas
> @fin

Ha finalizado el ingreso de texto.


El texto contiene 2 palabras que no están en el diccionario.
```


### Segunda etapa
Modifique el programa de la primer etapa para que levante el texto desde un archivo en texto plano ya escrito, por ejemplo `carta.txt` y haga la comprobación.
El programa no debe perder la funcionalidad adquirida en la primer etapa y debe ser capaz de realizar las dos opciones dependiendo la elección del usuario.

```bash
¡Bienvenido al TP1 del curso de programación!
1) Modo interactivo
2) Archivo externo

Su opción: 2

Escriba el nombre del archivo: carta.txt

Ha finalizado el ingreso del texto.

El texto contiene 2 palabras que no están en el diccionario.
```

> Tip: Utilice el siguiente código para abrir el archivo. De esta forma, en caso que el archivo no se encuentre, el programa dará el mensaje de "No se encuentra el archivo <nombre>" en vez de cerrarse el programa.

```python
# filename es la variable que contiene el nombre del archivo a abrir
try:
    with open(filename) as f:
        # Sentencias de código
except FileNotFoundError:
    print(f"No se encuentra el archivo {filename}.")

```

Veremos **excepciones** mas adelante para profundizar en la sentencia vista arriba.

### Tercera etapa
Modifique el programa para que sea capaz de mostrarle al usuario la palabra que no se encuentra en el diccionario y dé la oportunidad de:
- Re escribir la palabra
- Agregarla al diccionario de palabras
- Ignorar y seguir


```bash
¡Bienvenido al TP1 del curso de programación!

1) Modo interactivo
2) Archivo externo

Su opción: 1
Usted ha ingresado al modo interactivo.

> Esto es un texto de prueba para verificar el funcionamiento.
> Debe poder leer un texto así.
> prueva. zaasdfj
> @fin

La palabra prueva no se encuentra en el diccionario.
¿Qué desea hacer?

1. Agregarla al diccionario
2. Corregir palabra
3. Ignorar y seguir

Su opción: 2
Escriba nuevamente la palabra: prueba

--

La palabra zaasdfj no se encuentra en el diccionario.
¿Qué desea hacer?

1. Agregarla al diccionario
2. Corregir palabra
3. Ignorar y seguir

Su opción: 2
Escriba nuevamente la palabra: finalizar

El texto no contiene palabras que no están en el diccionario.
```

## Forma y fecha de entrega

La fecha final de entrega es el viernes 14 de julio de 2023 si no se llega a completarlo, entregue hasta donde llegó indicando lo que falta.

La forma de entrega es comprimir el archivo.py y enviarlo como adjunto a _cgiambruni@gmail.com_.

-----

<img src="../practicas/img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 90%">