#Aplicación de Conceptos de POO en Python Semana 06 Monica Rogel

# Clase base: Persona
class Persona:
    """
    Clase base que representa una persona.
    Incluye:
    - Encapsulación: atributo privado (__nombre).
    - Polimorfismo: método mostrar_informacion diseñado para ser sobrescrito.
    """
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.edad = edad  # Atributo público

    def obtener_nombre(self):
        return self.__nombre

    def mostrar_informacion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.edad}"


# Clase derivada: Estudiante
class Estudiante(Persona):
    """
    Clase derivada de Persona que representa un estudiante.
    Incluye:
    - Herencia: Extiende la clase base Persona.
    - Polimorfismo: Sobrescribe el método mostrar_informacion.
    """
    def __init__(self, nombre, edad, grado, cuenta_estudiante):
        super().__init__(nombre, edad)  # Herencia
        self.grado = grado
        self.cuenta_estudiante = cuenta_estudiante  # Asociación con CuentaEstudiante

    def mostrar_informacion(self):
        return (f"Estudiante: {self.obtener_nombre()}, Edad: {self.edad}, "
                f"Grado: {self.grado}, Saldo disponible: ${self.cuenta_estudiante.obtener_saldo():.2f}")


# Clase derivada: Profesor
class Profesor(Persona):
    """
    Clase derivada de Persona que representa un profesor.
    Incluye:
    - Herencia: Extiende la clase base Persona.
    - Polimorfismo: Sobrescribe el método mostrar_informacion.
    """
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def mostrar_informacion(self):
        return f"Profesor: {self.obtener_nombre()}, Edad: {self.edad}, Especialidad: {self.especialidad}"


# Clase para gestionar el saldo del estudiante
class CuentaEstudiante:
    """
    Clase que gestiona el saldo de un estudiante.
    Incluye:
    - Encapsulación: Atributo __saldo es privado.
    """
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositado: ${cantidad:.2f}. Nuevo saldo: ${self.__saldo:.2f}")
        else:
            print("La cantidad debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retirado: ${cantidad:.2f}. Nuevo saldo: ${self.__saldo:.2f}")
        else:
            print("Fondos insuficientes.")

    def obtener_saldo(self):
        return self.__saldo


# Parte principal del programa
if __name__ == "__main__":
    print("=== Gestión de Personas ===")

    # Captura segura de datos del estudiante
    while True:
        try:
            nombre_estudiante = input("Ingrese el nombre del estudiante: ")
            edad_estudiante = int(input("Ingrese la edad del estudiante: "))
            grado_estudiante = input("Ingrese el grado del estudiante: ")
            saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta del estudiante: "))
            break
        except ValueError:
            print("Error: Por favor, ingrese datos válidos.")

    cuenta = CuentaEstudiante(saldo_inicial)
    estudiante = Estudiante(nombre_estudiante, edad_estudiante, grado_estudiante, cuenta)

    # Captura segura de datos del profesor
    while True:
        try:
            nombre_profesor = input("Ingrese el nombre del profesor: ")
            edad_profesor = int(input("Ingrese la edad del profesor: "))
            especialidad_profesor = input("Ingrese la especialidad del profesor: ")
            break
        except ValueError:
            print("Error: Por favor, ingrese datos válidos.")

    profesor = Profesor(nombre_profesor, edad_profesor, especialidad_profesor)

    # Mostrar información
    print("\n=== Información ===")
    print(estudiante.mostrar_informacion())
    print(profesor.mostrar_informacion())

    # Gestión de la cuenta del estudiante
    print("\n=== Gestión de la cuenta del estudiante ===")
    print(f"Saldo inicial: ${cuenta.obtener_saldo():.2f}")
    historial_operaciones = []  # Registro de operaciones realizadas

    while True:
        print("\nOpciones: ")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuenta.depositar(cantidad)
                historial_operaciones.append(f"Depósito de ${cantidad:.2f}")
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico.")
        elif opcion == "2":
            try:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)
                historial_operaciones.append(f"Retiro de ${cantidad:.2f}")
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico.")
        elif opcion == "3":
            print(f"Saldo actual: ${cuenta.obtener_saldo():.2f}")
        elif opcion == "4":
            # Confirmación para salir
            confirmar = input("¿Está seguro de que desea salir? (s/n): ").lower()
            if confirmar == "s":
                print("Gracias por usar el sistema.")
                print("\n=== Resumen de operaciones ===")
                for operacion in historial_operaciones:
                    print(f"- {operacion}")
                print(f"Saldo final: ${cuenta.obtener_saldo():.2f}")
                break
        else:
            print("Opción no válida. Intente de nuevo.")
