"""Semana 13
Tarea: Conceptos fundamentales de interfaces gráficas de usuario
Monica Rogel"""

# Importación de módulos necesarios
import tkinter as tk  # Para la interfaz gráfica
from tkinter import ttk, messagebox  # Widgets temáticos y ventanas de diálogo
import re  # Para validar expresiones regulares (correo electrónico)


# Función para validar el formato de un correo electrónico
def validar_correo(correo):
    """
    Valida si un correo electrónico tiene un formato válido utilizando una expresión regular.
    Retorna True si el correo es válido, False en caso contrario.
    """
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', correo)


# Función para validar que un nombre solo contenga letras y espacios
def validar_nombre(nombre):
    """
    Valida que un nombre solo contenga letras y espacios.
    Retorna True si el nombre es válido, False en caso contrario.
    """
    return all(x.isalpha() or x.isspace() for x in nombre)


# Función para formatear un nombre con mayúsculas iniciales
def formatear_nombre(nombre):
    """
    Formatea un nombre para que cada palabra comience con mayúscula.
    Retorna el nombre formateado.
    """
    return ' '.join(p.capitalize() for p in nombre.split())


# Función para actualizar el estado de los botones según los registros en la tabla
def actualizar_botones():
    if len(tabla.get_children()) == 0:
        btn_eliminar.config(state=tk.DISABLED)
        btn_modificar.config(state=tk.DISABLED)
        btn_limpiar.config(state=tk.DISABLED)
    else:
        btn_eliminar.config(state=tk.NORMAL)
        btn_modificar.config(state=tk.NORMAL)
        btn_limpiar.config(state=tk.NORMAL)


# Función para agregar un nuevo usuario a la tabla
def agregar_usuario():
    nombre_completo = formatear_nombre(entrada_nombre_completo.get().strip())
    correo = entrada_correo.get().strip()
    contraseña = entrada_contraseña.get().strip()
    confirmar_contraseña = entrada_confirmar_contraseña.get().strip()

    if not nombre_completo or not correo or not contraseña or not confirmar_contraseña:
        messagebox.showwarning("Entrada inválida", "Todos los campos son obligatorios.")
        return

    if not validar_nombre(nombre_completo):
        messagebox.showwarning("Entrada inválida", "El nombre y apellido solo deben contener letras.")
        return

    if not validar_correo(correo):
        messagebox.showwarning("Entrada inválida", "Ingrese un correo electrónico válido.")
        return

    if len(contraseña) < 6:
        messagebox.showwarning("Seguridad de contraseña", "La contraseña debe tener al menos 6 caracteres.")
        return

    if contraseña != confirmar_contraseña:
        messagebox.showwarning("Entrada inválida", "Las contraseñas no coinciden.")
        return

    tabla.insert("", tk.END, values=(nombre_completo, correo, "********"))

    entrada_nombre_completo.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_contraseña.delete(0, tk.END)
    entrada_confirmar_contraseña.delete(0, tk.END)

    actualizar_botones()
    messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente.")


# Función para eliminar un usuario seleccionado de la tabla
def eliminar_usuario():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Selección inválida", "Seleccione un usuario para eliminar.")
        return

    for item in seleccionado:
        tabla.delete(item)

    actualizar_botones()


# Función para eliminar todos los usuarios de la tabla
def limpiar_usuarios():
    if messagebox.askyesno("Confirmación", "¿Desea eliminar todos los registros?"):
        for item in tabla.get_children():
            tabla.delete(item)

    actualizar_botones()


# Función para modificar un usuario seleccionado
def modificar_usuario():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Selección inválida", "Seleccione un usuario para modificar.")
        return

    valores = tabla.item(seleccionado[0], "values")
    entrada_nombre_completo.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_nombre_completo.insert(0, valores[0])
    entrada_correo.insert(0, valores[1])
    tabla.delete(seleccionado[0])
    actualizar_botones()


# Función para salir de la aplicación
def salir_aplicacion():
    if messagebox.askyesno("Salir", "¿Seguro que desea salir?"):
        ventana.quit()


# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Usuarios")
ventana.geometry("600x450")
ventana.resizable(False, False)
ventana.configure(bg="#d9f2ff")
ventana.update_idletasks()
anchura = ventana.winfo_width()
altura = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (anchura // 2)
y = (ventana.winfo_screenheight() // 2) - (altura // 2)
ventana.geometry(f"{anchura}x{altura}+{x}+{y}")
ventana.protocol("WM_DELETE_WINDOW", lambda: None)

# Mensaje de bienvenida
mensaje_bienvenida = ttk.Label(ventana, text="¡Bienvenido/a! Soy Mónica, tu asistente de registro.",
                               font=("Arial", 12, "bold"), background="#d9f2ff", foreground="#003366")
mensaje_bienvenida.pack(pady=10)

# Campos de entrada
ttk.Label(ventana, text="Nombre y Apellido:", background="#d9f2ff").pack()
entrada_nombre_completo = ttk.Entry(ventana, width=40)
entrada_nombre_completo.pack()

ttk.Label(ventana, text="Correo:", background="#d9f2ff").pack()
entrada_correo = ttk.Entry(ventana, width=40)
entrada_correo.pack()

ttk.Label(ventana, text="Contraseña:", background="#d9f2ff").pack()
entrada_contraseña = ttk.Entry(ventana, width=40, show="*")
entrada_contraseña.pack()

ttk.Label(ventana, text="Confirmar Contraseña:", background="#d9f2ff").pack()
entrada_confirmar_contraseña = ttk.Entry(ventana, width=40, show="*")
entrada_confirmar_contraseña.pack()

# Botones
frame_botones = tk.Frame(ventana, bg="#d9f2ff")
frame_botones.pack(pady=5)

btn_agregar = ttk.Button(frame_botones, text="Registrar", command=agregar_usuario)
btn_agregar.grid(row=0, column=0, padx=5)

btn_modificar = ttk.Button(frame_botones, text="Modificar", command=modificar_usuario, state=tk.DISABLED)
btn_modificar.grid(row=0, column=1, padx=5)

btn_eliminar = ttk.Button(frame_botones, text="Eliminar", command=eliminar_usuario, state=tk.DISABLED)
btn_eliminar.grid(row=0, column=2, padx=5)

btn_limpiar = ttk.Button(frame_botones, text="Eliminar Todos", command=limpiar_usuarios, state=tk.DISABLED)
btn_limpiar.grid(row=0, column=3, padx=5)

btn_salir = ttk.Button(frame_botones, text="Salir", command=salir_aplicacion)
btn_salir.grid(row=0, column=4, padx=5)

# Tabla de usuarios
tabla_frame = tk.Frame(ventana)
tabla_frame.pack(pady=5, fill=tk.BOTH, expand=True)

tabla = ttk.Treeview(tabla_frame, columns=("Nombre y Apellido", "Correo", "Contraseña"), show="headings")
tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
tabla.heading("Correo", text="Correo")
tabla.heading("Contraseña", text="Contraseña")
tabla.pack(fill=tk.BOTH, expand=True)

# Ejecución de la aplicación
ventana.mainloop()
