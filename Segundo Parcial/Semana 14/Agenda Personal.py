"""Semana 14
Tarea:  Creación de una Aplicación de Agenda Personal
Monica Rogel"""

import requests
import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from tkinter import messagebox


# --------------------- Función para centrar la ventana ---------------------
def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    # Suponiendo que la barra de tareas ocupa aproximadamente 50 píxeles
    y_offset = 50
    x = (screen_width // 2) - (ancho // 2)
    y = ((screen_height - y_offset) // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


# --------------------- Funciones de reloj ---------------------
def actualizar_reloj():
    ahora = datetime.now().strftime("%H:%M:%S")
    lbl_reloj.config(text=f"Hora actual: {ahora}")
    root.after(1000, actualizar_reloj)


# --------------------- Funciones de feriados y eventos ---------------------
def obtener_feriados_ecuador(anio):
    url = f"https://date.nager.at/api/v3/PublicHolidays/{anio}/EC"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", f"No se pudo obtener feriados para el año {anio}")
        return []


def marcar_feriados():
    anio = int(spin_anio.get())
    # Limpiar eventos previos con etiqueta "feriado"
    for ev in cal.get_calevents(tag="feriado"):
        cal.calevent_remove(ev)
    feriados = obtener_feriados_ecuador(anio)
    for feriado in feriados:
        fecha_str = feriado['date']
        fecha_dt = datetime.strptime(fecha_str, "%Y-%m-%d")
        celebracion = feriado['localName']
        cal.calevent_create(fecha_dt, celebracion, "feriado")
    cal.tag_config("feriado", background="red", foreground="white")
    messagebox.showinfo("Información", f"Feriados del {anio} marcados en el calendario.")
    cargar_eventos_dia()


def mostrar_info_fecha():
    fecha_sel_str = cal.get_date()
    fecha_sel = datetime.strptime(fecha_sel_str, "%Y-%m-%d").date()
    eventos_ids = cal.get_calevents(date=fecha_sel)
    if eventos_ids:
        detalles = ""
        for ev in eventos_ids:
            detalles += cal.calevent_cget(ev, "text") + "\n"
        messagebox.showinfo("Detalles de la fecha", f"En {fecha_sel.strftime('%Y-%m-%d')}:\n{detalles}")
    else:
        messagebox.showinfo("Detalles de la fecha", f"En {fecha_sel.strftime('%Y-%m-%d')} no hay eventos marcados.")


def agregar_evento_personal():
    fecha_sel_str = cal.get_date()
    fecha_sel = datetime.strptime(fecha_sel_str, "%Y-%m-%d")
    tipo = var_tipo.get()
    descripcion = entry_descripcion.get().strip()
    if not tipo or not descripcion:
        messagebox.showwarning("Advertencia", "Seleccione el tipo de evento y escriba una descripción.")
        return
    hora_actual = datetime.now().strftime("%H:%M:%S")
    evento_texto = f"{tipo}: {descripcion} (Creado a las {hora_actual})"
    cal.calevent_create(fecha_sel, evento_texto, "personal")
    cal.tag_config("personal", background="blue", foreground="white")
    messagebox.showinfo("Éxito", "Evento personal agregado.")
    entry_descripcion.delete(0, tk.END)
    cargar_eventos_dia()


def cargar_eventos_dia():
    lista_eventos.delete(0, tk.END)
    global eventos_mapping
    eventos_mapping = {}
    fecha_sel_str = cal.get_date()
    fecha_sel = datetime.strptime(fecha_sel_str, "%Y-%m-%d").date()
    eventos_ids = cal.get_calevents(date=fecha_sel)
    for idx, ev in enumerate(eventos_ids):
        texto = cal.calevent_cget(ev, "text")
        lista_eventos.insert(tk.END, texto)
        eventos_mapping[idx] = ev


def mostrar_alerta_personalizada(msg):
    alerta = tk.Toplevel(root)
    alerta.title("Advertencia")
    alerta.config(bg="red")
    ancho_alerta, alto_alerta = 300, 150
    root.update_idletasks()
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    x = root_x + (root_width - ancho_alerta) // 2
    y = root_y + (root_height - alto_alerta) // 2
    alerta.geometry(f"{ancho_alerta}x{alto_alerta}+{x}+{y}")

    tk.Label(alerta, text=msg, bg="red", fg="white", font=("Arial", 10, "bold")).pack(padx=20, pady=20)
    tk.Button(alerta, text="OK", command=alerta.destroy).pack(pady=10)
    alerta.transient(root)
    alerta.grab_set()
    root.wait_window(alerta)


def eliminar_evento():
    seleccion = lista_eventos.curselection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione al menos un evento para eliminar.")
        return

    eliminados = False
    no_eliminados = []
    for idx in seleccion[::-1]:
        ev_id = eventos_mapping.get(idx)
        if ev_id is not None:
            etiquetas = cal.calevent_cget(ev_id, "tags")
            if "personal" in etiquetas:
                cal.calevent_remove(ev_id)
                eliminados = True
            else:
                no_eliminados.append(cal.calevent_cget(ev_id, "text"))
    if no_eliminados:
        mostrar_alerta_personalizada("No se pueden eliminar feriado:\n" + "\n".join(no_eliminados))
    if eliminados:
        messagebox.showinfo("Éxito", "Evento(s) personal(es) eliminado(s).")
    cargar_eventos_dia()


def on_date_change(event):
    cargar_eventos_dia()


# --------------------- INTERFAZ GRÁFICA ---------------------
root = tk.Tk()
root.title("Agenda Personal")
# Colores de fondo y dimensiones ajustadas para mejor percepción
bg_color = "#e6f2ff"  # Fondo principal (azul claro)
frame_color = "#cce6ff"  # Fondo de frames
root.configure(bg=bg_color)

ancho_principal, alto_principal = 600, 700
root.geometry(f"{ancho_principal}x{alto_principal}")
root.resizable(False, False)
centrar_ventana(root, ancho_principal, alto_principal)

# Limitar la interacción del usuario: deshabilitar maximizar y cerrar (solo se permite minimizar)
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Reloj digital en la parte superior derecha
lbl_reloj = tk.Label(root, text="", font=("Helvetica", 14), bg=bg_color)
lbl_reloj.grid(row=0, column=0, padx=10, pady=5, sticky="ne")
actualizar_reloj()

# Frame superior: Año y Calendario
frame_superior = tk.Frame(root, bg=frame_color, bd=2, relief="groove")
frame_superior.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

frame_anio = tk.Frame(frame_superior, bg=frame_color)
frame_anio.grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Label(frame_anio, text="Seleccione el año: ", bg=frame_color).pack(side=tk.LEFT)
anio_actual = datetime.now().year
spin_anio = tk.Spinbox(frame_anio, from_=2000, to=2050, width=5)
spin_anio.delete(0, tk.END)
spin_anio.insert(0, str(anio_actual))
spin_anio.pack(side=tk.LEFT)

cal = Calendar(frame_superior, selectmode="day", year=anio_actual,
               month=datetime.now().month, day=datetime.now().day, date_pattern="yyyy-mm-dd")
cal.grid(row=1, column=0, pady=10, padx=5, sticky="nsew")
cal.bind("<<CalendarSelected>>", on_date_change)

btn_marcar = tk.Button(frame_superior, text="Marcar Feriados", command=marcar_feriados, bg="#66b3ff")
btn_marcar.grid(row=2, column=0, pady=5, padx=5, sticky="ew")

# Frame intermedio: Agregar evento personal
frame_evento = tk.LabelFrame(root, text="Agregar Evento Personal", bg=frame_color, fg="black", bd=2, relief="groove")
frame_evento.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

tk.Label(frame_evento, text="Tipo de Evento:", bg=frame_color).grid(row=0, column=0, sticky="e", padx=5, pady=5)
opciones_evento = ["Trabajo", "Educación", "Cumpleaños", "Evento Familiar", "Evento Social", "Salud", "Otros"]
var_tipo = tk.StringVar(frame_evento)
var_tipo.set(opciones_evento[0])
option_menu = tk.OptionMenu(frame_evento, var_tipo, *opciones_evento)
option_menu.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_evento, text="Descripción:", bg=frame_color).grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_descripcion = tk.Entry(frame_evento, width=30)
entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

btn_guardar_evento = tk.Button(frame_evento, text="Guardar Evento Personal", command=agregar_evento_personal,
                               bg="#66b3ff")
btn_guardar_evento.grid(row=2, column=0, columnspan=2, pady=10, padx=5)

# Frame inferior: Lista de eventos y botón de eliminación
frame_inferior = tk.LabelFrame(root, text="Eventos del día seleccionado", bg=frame_color, fg="black", bd=2,
                               relief="groove")
frame_inferior.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

scrollbar = tk.Scrollbar(frame_inferior, orient="vertical")
lista_eventos = tk.Listbox(frame_inferior, width=50, height=6, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_eventos.yview)
scrollbar.grid(row=0, column=1, sticky="ns", padx=5, pady=5)
lista_eventos.grid(row=0, column=0, padx=5, pady=5)

btn_eliminar = tk.Button(frame_inferior, text="Eliminar Evento(s)", command=eliminar_evento, bg="#ff6666", fg="white")
btn_eliminar.grid(row=1, column=0, columnspan=2, pady=5)

# Botón Salir en la parte inferior derecha
btn_salir = tk.Button(root, text="Salir", command=root.destroy, bg="#ff6666", fg="white")
btn_salir.grid(row=4, column=0, padx=10, pady=10, sticky="se")

# Configuración de pesos para que se adapten los frames
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
frame_superior.grid_rowconfigure(1, weight=1)
frame_superior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)
frame_inferior.grid_columnconfigure(0, weight=1)

eventos_mapping = {}
cargar_eventos_dia()

root.mainloop()
