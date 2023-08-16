# Laboratorio 1
En este laboratorio usted aprenderá sobre:
- Conceptos de archivos csv

# Archivos CSV
Los archivos `.csv` (Comma separated values) que significa valores separados por comas, son un tipo de documento en formato abierto sencillo para representar datos en forma de tabla, en las que las columnas se separan por comas y las filas por saltos de líneas.

Por ejemplo, si queremos representar la siguiente tabla en formato `csv` 

| Marca     | Modelo | Año  | Precio  | Origen |
|-----------|--------|------|---------|--------|
| Ford      | Fiesta | 2013 | 2000.00 | México |
| Chevrolet | Onix   | 2015 | 2190.12 | Brasil |
| Peugeot   | 208 GT | 2019 | 2590.99 | Brasil |

un archivo `csv` que contiene esa info es el siguiente:

```
Marca,Modelo,Año,Precio,Origen
Ford,Fiesta,2013,2000.00,México
Chevrolet,Onix,2015,2190.12,Brasil
Peugeot,208 GT,2019,2590.99,Brasil
```
Observe que se usa la primer línea para definir el nombre de las columnas. Y el resto de líneas contiene los datos. Si bien esto es opcional, es frecuente verlo.

En Python tenemos la biblioteca [csv](https://docs.python.org/es/3/library/csv.html) donde nos brinda métodos para poder manipular archivos `csv`.

## Escribiendo un archivo csv en Python

### Ejemplo Registro de gastos

Supongamos que queremos escribir un programa para registrar nuestros gastos y queremos que la info se guarde en un archivo. Lo correcto sería usar algún formato estándar para guardar la info como puede ser [csv](https://es.wikipedia.org/wiki/Valores_separados_por_comas), [json](https://es.wikipedia.org/wiki/JSON), [yaml](https://es.wikipedia.org/wiki/YAML), etc. En este caso vamos a usar el mas sencillo de todos, el csv.

El programa nos soliciará el concepto del gasto y el monto y luego agregará esa información al archivo llamado `gastos.csv`. La carga de información terminará cuando el usuario ingrese la palabra `salir`.

Nuestro archivo `csv` constará de dos columnas: "Concepto" y "Monto". Por ejemplo:

| Concepto                   	| Monto 	|
|----------------------------	|-------	|
| Carga Sube                 	| 500.00   	|
|  Almuerzo lunes            	| 950.00   	|
| Regalo de cumple para Luca 	| 10500.00 	|

En nuestro archivo se verá de la siguiente manera:

```csv
Concepto,Monto
Carga de Sube,500.00
Almuerzo día Lunes,950.00
Regalo cumple para Luca, 10500.00
```

A continuación se muestra un programa de ejemplo que cumple con lo solicitado. Analice y estudie el código. ¿Qué cosas ve que podría mejorar?

```python
# Importo la biblioteca csv
''' Programa para registro de gastos del curso de prorgamación 2023
del CFL 410 Omar Nuñez
'''

import csv

def agregar_gasto(concepto, monto):    
    with open('gastos.csv', 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([concepto, monto])
    print("Gasto registrado exitosamente.")

# main
while True:
    concepto = input("Ingresa el concepto del gasto (o 'salir' para terminar): ")
    if concepto.lower() == 'salir':
        break
    monto = float(input("Ingresa el monto del gasto: "))
    agregar_gasto(concepto, monto)

print("Finalizado la carga de datos.")
```

### Leer un archivo csv

En el ejemplo anterior vimos un ejemplo para _escribir_ en un archivo `csv`. Pero veremos un ejemplo de como poder _leer_ o __parsear__ (del inglés _parse_).
>En el contexto de la programación, __"parsear"__ se utiliza para describir la acción de analizar una entrada, como un archivo de texto o una cadena, y extraer información útil o relevante siguiendo una estructura predefinida.

### Ejemplo lista de tareas

En este caso tenemos un archivo csv llamado `tareas.csv` que contiene una lista de tareas pendientes:

```
tarea,fecha
Comprar yerba,2023-08-10
Hacer ejercicio 40 minutos,2023-08-11
Estudiar para el curso,2023-08-12
```

Se nos pide hacer un programa que lea el archivo csv y lo muestre en pantalla la lista de tarea junto con las fechas. Analice el siguiente código:

```python
import csv

with open('tareas.csv', 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        tarea = fila['tarea']
        fecha = fila['fecha']
        print(f"Tarea: {tarea}, Fecha: {fecha}")

```

Con este ejemplo como base y la posibilidad de buscar en internet cualquier duda que surja:
- Realice un programa que, parseé el archivo `gastos.csv` e informe el mayor gasto que ha tenido.



-----

<img src="../practicas/img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 90%">