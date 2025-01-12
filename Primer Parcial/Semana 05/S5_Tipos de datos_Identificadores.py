#Calculadora de Áreas y Perímetros Semana 05 Monica Rogel

"""
Programa: Calculadora de Áreas y Perímetros
Descripción: Este programa calcula el área y el perímetro de figuras geométricas simples (cuadrado, rectángulo, círculo).
Se utilizan tipos de datos como float, string y boolean, y se siguen las convenciones de nombres en Python.
"""

import math  # Importamos math para realizar operaciones matemáticas, como pi.


# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado: float) -> float:
    """
    Calcula el área de un cuadrado.
    Parámetro:
        lado (float): Longitud del lado del cuadrado.
    Retorna:
        float: Área del cuadrado.
    """
    return lado ** 2


# Función para calcular el perímetro de un cuadrado
def calcular_perimetro_cuadrado(lado: float) -> float:
    """
    Calcula el perímetro de un cuadrado.
    Parámetro:
        lado (float): Longitud del lado del cuadrado.
    Retorna:
        float: Perímetro del cuadrado.
    """
    return 4 * lado


# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo.
    Parámetros:
        base (float): Longitud de la base del rectángulo.
        altura (float): Longitud de la altura del rectángulo.
    Retorna:
        float: Área del rectángulo.
    """
    return base * altura


# Función para calcular el perímetro de un rectángulo
def calcular_perimetro_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el perímetro de un rectángulo.
    Parámetros:
        base (float): Longitud de la base del rectángulo.
        altura (float): Longitud de la altura del rectángulo.
    Retorna:
        float: Perímetro del rectángulo.
    """
    return 2 * (base + altura)


# Función para calcular el área de un círculo
def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo.
    Parámetro:
        radio (float): Radio del círculo.
    Retorna:
        float: Área del círculo.
    """
    return math.pi * (radio ** 2)


# Función para calcular el perímetro (circunferencia) de un círculo
def calcular_perimetro_circulo(radio: float) -> float:
    """
    Calcula el perímetro (circunferencia) de un círculo.
    Parámetro:
        radio (float): Radio del círculo.
    Retorna:
        float: Perímetro del círculo.
    """
    return 2 * math.pi * radio


# Función para mostrar el menú de opciones
def mostrar_menu():
    """
    Muestra las opciones disponibles en el programa.
    """
    print("\n--- Calculadora de Áreas y Perímetros ---")
    print("1. Calcular área y perímetro de un cuadrado")
    print("2. Calcular área y perímetro de un rectángulo")
    print("3. Calcular área y perímetro de un círculo")
    print("4. Salir")


# Programa principal
if __name__ == "__main__":
    continuar = True  # Booleano para controlar si el programa sigue ejecutándose

    while continuar:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            lado = float(input("Ingresa la longitud del lado del cuadrado: "))
            print(f"Área del cuadrado: {calcular_area_cuadrado(lado):.2f}")
            print(f"Perímetro del cuadrado: {calcular_perimetro_cuadrado(lado):.2f}")

        elif opcion == "2":
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            print(f"Área del rectángulo: {calcular_area_rectangulo(base, altura):.2f}")
            print(f"Perímetro del rectángulo: {calcular_perimetro_rectangulo(base, altura):.2f}")

        elif opcion == "3":
            radio = float(input("Ingresa el radio del círculo: "))
            print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
            print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}")

        elif opcion == "4":
            print("Gracias por usar la calculadora. ¡Adiós!")
            continuar = False  # Cambiamos el valor del booleano para salir del programa

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
