# Semana 04 _ Monica Rogel Q

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    # Creamos una lista vacía para almacenar las temperaturas
    temperaturas = []
    print("Introduce las temperaturas diarias de la semana:")

    # Usamos un bucle para pedir las temperaturas de los 7 días
    for i in range(7):
        while True:  # Bucle para asegurar que el usuario ingrese un número válido
            try:
                # Solicitamos al usuario que ingrese la temperatura para el día actual
                temp = float(input(f"Día {i + 1}: "))
                # Si el dato es válido, lo agregamos a la lista
                temperaturas.append(temp)
                break  # Salimos del bucle si se ingresó un dato correcto
            except ValueError:
                # Si ocurre un error al convertir a número, mostramos un mensaje
                print("Por favor, introduce un número válido.")
    # Devolvemos la lista completa de temperaturas
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    # Calculamos la suma de todas las temperaturas de la lista
    suma = sum(temperaturas)
    # Dividimos la suma entre el número de días (7) para obtener el promedio
    promedio = suma / len(temperaturas)
    # Devolvemos el promedio calculado
    return promedio


# Función principal que coordina el programa
def main():
    print("Programa para calcular el promedio semanal de temperaturas")

    # Llamamos a la función para que el usuario ingrese las temperaturas
    temperaturas = ingresar_temperaturas()

    # Llamamos a la función para calcular el promedio con las temperaturas ingresadas
    promedio = calcular_promedio(temperaturas)

    # Mostramos las temperaturas ingresadas al usuario
    print("\nLas temperaturas ingresadas son:", temperaturas)
    # Mostramos el promedio semanal calculado con 2 decimales
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")


# Esta parte asegura que el programa solo se ejecute si se ejecuta directamente
if __name__ == "__main__":
    # Llamamos a la función principal para iniciar el programa
    main()
