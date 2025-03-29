"""Semana 15
Tarea: Conceptos fundamentales de manejo de eventos
Monica Rogel"""

import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Funciones para manejar eventos
# -------------------------------

def add_task():
    """Añade una nueva tarea a la lista si el campo de entrada no está vacío."""
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

def complete_task():
    """Marca la tarea seleccionada como completada agregando un ✔ al final."""
    try:
        task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(task_index)
        if "✔" not in task:
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, task + " ✔")
        else:
            messagebox.showwarning("Advertencia", "Esta tarea ya está completada.")
    except IndexError:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

def delete_task():
    """Elimina la tarea seleccionada de la lista."""
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

def clear_tasks():
    """Elimina todas las tareas si hay al menos una."""
    if listbox_tasks.size() == 0:
        messagebox.showwarning("Advertencia", "No hay tareas para eliminar.")
        return
    if messagebox.askyesno("Confirmación", "¿Eliminar todas las tareas?"):
        listbox_tasks.delete(0, tk.END)

# -------------------------------
# Configuración de la interfaz
# -------------------------------
root = tk.Tk()
root.title("Lista de Tareas  <<--Monica Rogel-->>")
root.config(bg="#f0f0f0")
root.geometry("400x450")  # Se redujo la altura de la ventana
root.resizable(False, False)

# Centrar la ventana en la pantalla
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 450
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Etiqueta para el campo de entrada
label_task = tk.Label(root, text="Escribe una nueva tarea:", bg="#f0f0f0", font=("Calibri", 12))
label_task.pack(pady=5)

# Campo de entrada
entry_task = tk.Entry(root, width=40, font=("Calibri", 12))
entry_task.pack(pady=5)

# Lista de tareas
listbox_tasks = tk.Listbox(root, width=40, height=15, font=("Calibri", 12))
listbox_tasks.pack(pady=5)

# Frame para los botones
frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=5)

# Botones
button_add_task = tk.Button(frame_buttons, text="Agregar", command=add_task, bg="#4caf50", fg="white", font=("Calibri", 10))
button_add_task.grid(row=0, column=0, padx=5)

button_complete_task = tk.Button(frame_buttons, text="Completar", command=complete_task, bg="#2196f3", fg="white", font=("Calibri", 10))
button_complete_task.grid(row=0, column=1, padx=5)

button_delete_task = tk.Button(frame_buttons, text="Eliminar", command=delete_task, bg="#f44336", fg="white", font=("Calibri", 10))
button_delete_task.grid(row=0, column=2, padx=5)

button_clear_tasks = tk.Button(frame_buttons, text="Eliminar Todas", command=clear_tasks, bg="#9e9e9e", fg="white", font=("Calibri", 10))
button_clear_tasks.grid(row=0, column=3, padx=5)

# Permitir agregar tareas con Enter
entry_task.bind("<Return>", lambda event: add_task())

# Iniciar el bucle principal
root.mainloop()
