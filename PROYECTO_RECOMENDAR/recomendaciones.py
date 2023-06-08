import tkinter as tk

ventana_principal = tk.Tk()
ventana_principal.geometry("1205x650")
ventana_principal.title("Comparador y Recomendador de Aseguradoras en Colombia")
ventana_principal.resizable(0, 0)
ventana_principal.config(bg="white")

frame_izquierdo = tk.Frame(ventana_principal)
frame_izquierdo.config(bg="white", bd=5, relief="groove", width=555, height=580)
frame_izquierdo.place(x=0, y=80)

frame_derecho = tk.Frame(ventana_principal)
frame_derecho.config(bg="white", bd=5, relief="groove", width=555, height=580)
frame_derecho.place(x=650, y=80)

frame_superior = tk.Frame(ventana_principal)
frame_superior.config(bg="light blue", bd=5, relief="ridge", width=1250, height=80)
frame_superior.place(x=0, y=0)

Label_recomendacion = tk.Label(ventana_principal, text="RECOMENDADOR")
Label_recomendacion.config(bg="light blue", fg="black", font=("Bodoni MT Black", 20,))
Label_recomendacion.place(x=480, y=20)

# Label y su texto de entrada.
Label_entrad1 = tk.Label(frame_izquierdo, text="Nombre")
Label_entrad1.config(bg="white", fg="black", font=("Bodoni MT Black", 10))
Label_entrad1.place(x=80, y=30)

entrada1 = tk.Entry(frame_izquierdo)
entrada1.place(x=200, y=30)

Label_entrad2 = tk.Label(frame_izquierdo, text="Edad")
Label_entrad2.config(bg="white", fg="black", font=("Bodoni MT Black", 10))
Label_entrad2.place(x=80, y=60)

entrada2 = tk.Entry(frame_izquierdo)
entrada2.place(x=200, y=60)

Label_entrad3 = tk.Label(frame_izquierdo, text="Sexo")
Label_entrad3.config(bg="white", fg="black", font=("Bodoni MT Black", 10))
Label_entrad3.place(x=80, y=90)

# Lista de opciones (Checklist)
opciones_sexo = ["Masculino", "Femenino"]

seleccion_sexo = tk.StringVar(value=opciones_sexo)
checklist_sexo = tk.Listbox(frame_izquierdo, listvariable=seleccion_sexo, height=2)
checklist_sexo.place(x=200, y=90)

Label_entrad4 = tk.Label(frame_izquierdo, text="Tipo de seguro")
Label_entrad4.config(bg="white", fg="black", font=("Bodoni MT Black", 10))
Label_entrad4.place(x=80, y=160)

# Lista de opciones (Checklist)
opciones_seguro = ["Seguro de vida", "Seguro de salud", "Seguro de auto", "Seguro de hogar", "Seguro de empresa", "Seguro de viaje"]

seleccion_seguro = tk.StringVar(value=opciones_seguro)
checklist_seguro = tk.Listbox(frame_izquierdo, listvariable=seleccion_seguro, selectmode=tk.MULTIPLE, height=4)
checklist_seguro.place(x=200, y=160)

# Botón de recomendaciones
boton_recomendaciones = tk.Button(frame_izquierdo, text="Obtener recomendaciones")
boton_recomendaciones.place(relx=0.5, rely=0.5, anchor="center")

ventana_principal.mainloop()
