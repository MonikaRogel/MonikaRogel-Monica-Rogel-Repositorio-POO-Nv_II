"""Semana 8 - Organización de un proyecto orientado a objetos - Dashboard
Estudiante: Monica Rogel"""

import os

def mostrar_codigo(ruta_script):
    # Convierto la ruta recibida a una ruta absoluta para trabajar de forma consistente.
    ruta_script_absoluta = os.path.abspath(ruta_script)

    # Verifico si el archivo existe. Si no, muestro un mensaje de error y salgo.
    if not os.path.exists(ruta_script_absoluta):
        print(f"c El archivo no existe: {ruta_script_absoluta}")
        return

    try:
        # Abro el archivo en modo lectura usando codificación UTF-8 para evitar problemas con caracteres especiales.
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except Exception as e:
        # Si ocurre cualquier error al leer el archivo, muestro un mensaje detallado.
        print(f"⚠️ Error al leer el archivo: {e}")

def mostrar_menu():
    # 🚀 Subo DOS niveles para llegar a la raíz del proyecto, de esta forma obtengo la ruta base.
    ruta_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    print(f"Ruta base detectada: {ruta_base}")

    # Defino las opciones del menú, cada una con la ruta correspondiente al script de cada semana.
    opciones = {
        '1': os.path.join(ruta_base, 'Primer Parcial/Semana 02/1.2.1. Ejemplo Tecnicas de Programacion Monica Rogel.py'),
        '2': os.path.join(ruta_base, 'Primer Parcial/Semana 03/Programación_Orientada_Objetos.py'),
        '3': os.path.join(ruta_base, 'Primer Parcial/Semana 03/Programación_Tradicional.py'),
        '4': os.path.join(ruta_base, 'Primer Parcial/Semana 04/EjemplosMundoReal_POO_S4_Monica Rogel.py'),
        '5': os.path.join(ruta_base, 'Primer Parcial/Semana 05/S5_Tipos de datos_Identificadores.py'),
        '6': os.path.join(ruta_base, 'Primer Parcial/Semana 06/Aplicación de Conceptos de POO en Python S6.py'),
        '7': os.path.join(ruta_base, 'Primer Parcial/Semana 07/Implementación de Constructores y Destructores en Python S7_Monica Rogel.py'),
        '8': os.path.join(ruta_base, 'Primer Parcial/Semana 08/Dashboard.py'),
    }

    # Inicio un bucle para mostrar el menú de opciones hasta que el usuario decida salir.
    while True:
        print("\n******** Menu Principal - Dashboard *************")
        # Itero sobre cada opción y muestro su clave y ruta.
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        # Solicito al usuario que elija un script o salga del programa.
        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = opciones[eleccion]
            print(f"Intentando abrir el archivo en: {ruta_script}")
            mostrar_codigo(ruta_script)
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

