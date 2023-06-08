import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Definir las preguntas y las recomendaciones asociadas
preguntas = [
    "Nombre",
    "Edad",
    "Ubicación",
    "Sexo",
    "Tipo de seguro",

]

recomendaciones = []


# Función para mostrar las recomendaciones
def mostrar_recomendaciones():
    respuestas = []
    for i in range(len(preguntas)):
        respuesta = respuesta_vars[i].get()
        respuestas.append(respuesta)

    recomendaciones_finales = []
    for i in range(len(respuestas)):
        if respuestas[i]:
            recomendaciones_finales.append(recomendaciones[i])

    if len(recomendaciones_finales) > 0:
        recomendaciones_texto = "\n\n".join(recomendaciones_finales)
        if respuestas[-1] == "Seguro de vida":  # Verificar si se seleccionó "Seguro de vida"
            recomendaciones_texto += "\n\nAXA COLPATRIA\n\nSeguros de Vida\n\nUn seguro de vida es la mejor forma de demostrarle a tu familia cuánto los quieres. Asegura su futuro.\n\n1- Plan Futuro Hoy\nAsegura un futuro lleno de prosperidad al lado de los que más quieres.\nAseguramos tu futuro y el de tu familia atendiendo tus necesidades de protección en caso de muerte. Con esta póliza tienes la opción de contratar algunas coberturas adicionales, de acuerdo con la etapa de la vida en la que te encuentres y a tu presupuesto. Este seguro posee dos elementos que componen la prima:\n\nProtección: valor de la prima de protección que cubre el riesgo asegurado.\nAhorro: corresponde al 25% de la prima de protección, sin contar el valor de las extraprimas.\n\nVentajas de adquirir este seguro\nCuentas con el respaldo de AXA COLPATRIA, una empresa con más de 50 años de experiencia en el mercado asegurador colombiano y el respaldo de AXA.\n\n2- Vida a mi Medida\nLa mejor forma de decirles cuánto los quieres.\nAseguramos tu futuro y el de tu familia. Con esta póliza atenderemos tus necesidades de protección con un amparo básico que te protege en caso de fallecimiento, brindándote anticipo de gastos exequiales, así como exoneración de pago de primas en caso de incapacidad total y permanente. Adicionalmente tendrás la opción de incluir coberturas adicionales, de acuerdo con tu presupuesto y necesidades de aseguramiento. Este seguro posee dos elementos que componen la prima:\n\nProtección: valor de la prima de protección que cubre el riesgo asegurado.\nAhorro: porcentaje de tu elección del valor total de la prima destinado para el ahorro.\n\nVentajas de adquirir este seguro\nAsistencia en viajes nacionales e internacionales.\nAsistencia en salud.\nAsistencia para mascotas.\nAseguramiento del cónyuge con descuento en la prima de la cobertura básica."

        messagebox.showinfo("Recomendaciones", recomendaciones_texto)
    else:
        messagebox.showinfo("Recomendaciones", "No hay recomendaciones en este momento.")

# Crear la ventana principal
window = tk.Tk()
window.title("Recomendador de Información")

# Crear las variables para almacenar las respuestas
respuesta_vars = []
for _ in preguntas:
    respuesta_vars.append(tk.StringVar())

# Crear los elementos de la interfaz
for i in range(len(preguntas)):
    label = tk.Label(window, text=preguntas[i])
    label.pack()

    if preguntas[i] == "Tipo de seguro":
        opciones = ["Seguro de vida", "Seguro de salud", "Seguro de auto", "Seguro de hogar", "Seguro de empresa", "Seguro de viaje", "Seguro "]
        checkbuttons = []
        for opcion in opciones:
            var = tk.StringVar()
            checkbutton = tk.Checkbutton(window, text=opcion, variable=var, onvalue=opcion, offvalue="")
            checkbutton.pack()
            checkbuttons.append(var)
        respuesta_vars[i] = checkbuttons  # Asignar la lista de variables a la variable de respuesta
    else:
        entry = tk.Entry(window, textvariable=respuesta_vars[i])
        entry.pack()

button = tk.Button(window, text="Obtener Recomendaciones", command=mostrar_recomendaciones)
button.pack()

# Iniciar el bucle de eventos de la interfaz
window.mainloop()
