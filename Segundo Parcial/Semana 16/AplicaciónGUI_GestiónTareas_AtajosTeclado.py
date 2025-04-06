"""Semana 16
Tarea: Aplicación GUI para Gestión de Tareas con Atajos de Teclado
Monica Rogel"""

import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Funciones para manejar eventos
# -------------------------------

def add_task():
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

def complete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(task_index)
        if "✔" not in task:
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, task + " ✔")
            listbox_tasks.itemconfig(task_index, {'bg':'lightgreen'})
        else:
            messagebox.showwarning("Advertencia", "Esta tarea ya está completada.")
    except IndexError:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

def clear_tasks():
    if listbox_tasks.size() == 0:
        messagebox.showwarning("Advertencia", "No hay tareas para eliminar.")
        return
    if messagebox.askyesno("Confirmación", "¿Eliminar todas las tareas?"):
        listbox_tasks.delete(0, tk.END)

def close_app(event=None):
    root.quit()

# -------------------------------
# Interfaz Gráfica
# -------------------------------
root = tk.Tk()
root.title("Lista de Tareas  <<--Monica Rogel-->>")
root.config(bg="#f0f0f0")
root.geometry("400x450")
root.resizable(False, False)

# Centrar la ventana
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - 400) // 2
y_position = (screen_height - 450) // 2
root.geometry(f"400x450+{x_position}+{y_position}")

# Widgets
label_task = tk.Label(root, text="Escribe una nueva tarea:", bg="#f0f0f0", font=("Calibri", 12))
label_task.pack(pady=5)

entry_task = tk.Entry(root, width=40, font=("Calibri", 12))
entry_task.pack(pady=5)

listbox_tasks = tk.Listbox(root, width=40, height=15, font=("Calibri", 12))
listbox_tasks.pack(pady=5)

frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=5)

# Botones
tk.Button(frame_buttons, text="Agregar", command=add_task, bg="#4caf50", fg="white", font=("Calibri", 10)).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Completar", command=complete_task, bg="#2196f3", fg="white", font=("Calibri", 10)).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Eliminar", command=delete_task, bg="#f44336", fg="white", font=("Calibri", 10)).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Eliminar Todas", command=clear_tasks, bg="#9e9e9e", fg="white", font=("Calibri", 10)).grid(row=0, column=3, padx=5)

# Atajos de teclado
entry_task.bind("<Return>", lambda e: add_task())
root.bind("<Control-c>", lambda e: complete_task())
root.bind("<Control-d>", lambda e: delete_task())
root.bind("<Delete>", lambda e: delete_task())
root.bind("<Escape>", close_app)

# Ejecutar app
root.mainloop()