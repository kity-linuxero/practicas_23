import tkinter as tk
from tkinter import ttk

# Dimensiones de la ventana (en píxeles)
ANCHO=350
ALTO=140

# Definimos app
app = tk.Tk()
app.title("Ejemplo clase")
app.config(width=ANCHO, height=ALTO)

# Definimos el texto
text1 = ttk.Label(text="Escriba su nombre: ")
text1.place(x=20,y=20)

# Definimos input
text_input = ttk.Entry()
#text_input.insert(0,"Escriba su nombre")
text_input.place(x=160, y=20)

# Definimos el texto del saludo
str_saludo = tk.StringVar()
ttk.Label()

# Observar el textvariable y se setea la variable que el label estará observando.
# Si la variable cambia, el label cambiará automáticamente
text_saludo = ttk.Label(app, textvariable = str_saludo)
# Ubicación de la contraseña
text_saludo.place(x=20,y=110)

# Función para saludar. Crea un nuevo label
def saludo():
    if len(text_input.get()):
        str_saludo.set(f"Hola {text_input.get()}")
    else:
        str_saludo.set(f"Hola amigazo!")


btn_saludo = ttk.Button(text="Saludame", command=saludo)
btn_saludo.place(x=20,y=50)

# Loop de la aplicación
app.mainloop()