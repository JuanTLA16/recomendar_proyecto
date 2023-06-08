import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Función para obtener el contenido de la entrada de texto
def obtener_texto():
    texto = entrada.get()
    print("Texto ingresado:", texto)

# Crear la entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Crear el botón para obtener el texto ingresado
boton = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()


