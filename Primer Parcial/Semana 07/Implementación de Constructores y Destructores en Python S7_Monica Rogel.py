#Ejemplo de uso de constructores y destructores en Python desarrollado por Monica Rogel

class Persona:
    """
    Clase que representa una persona con un nombre y una edad.
    """
    def __init__(self, nombre, edad):
        """
        Constructor que inicializa el nombre y la edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"[INFO] Persona creada: Nombre: {self.nombre}, Edad: {self.edad} años.")

    def __del__(self):
        """
        Destructor que muestra un mensaje indicando que la persona ha sido eliminada.
        """
        print(f"[INFO] Persona eliminada: Nombre: {self.nombre}.")


class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria.
    """
    def __init__(self, titular, saldo_inicial):
        """
        Constructor que inicializa el titular de la cuenta y el saldo inicial.
        """
        self.titular = titular  # Objeto de tipo Persona
        self.saldo = saldo_inicial
        print(f"[INFO] Cuenta bancaria creada: Titular: {self.titular.nombre}, Saldo inicial: ${self.saldo:.2f}.")

    def depositar(self, monto):
        """
        Método que permite depositar dinero en la cuenta.
        """
        self.saldo += monto
        print(f"[DEPÓSITO] Monto: ${monto:.2f} depositado. Saldo actual: ${self.saldo:.2f}.")

    def retirar(self, monto):
        """
        Método que permite retirar dinero de la cuenta.
        """
        if monto > self.saldo:
            print(f"[ERROR] Fondos insuficientes para retirar ${monto:.2f}. Saldo actual: ${self.saldo:.2f}.")
        else:
            self.saldo -= monto
            print(f"[RETIRO] Monto: ${monto:.2f} retirado. Saldo actual: ${self.saldo:.2f}.")

    def consultar_saldo(self):
        """
        Método que permite consultar el saldo actual de la cuenta.
        """
        print(f"[SALDO] Saldo actual de la cuenta: ${self.saldo:.2f}.")

    def __del__(self):
        """
        Destructor que simula el cierre de la cuenta bancaria.
        """
        print(f"[INFO] Cuenta cerrada: Titular: {self.titular.nombre}, Saldo final: ${self.saldo:.2f}.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una persona
    persona1 = Persona("Monica Rogel", 26)

    # Crear una cuenta bancaria para la persona
    cuenta1 = CuentaBancaria(persona1, 1000)

    # Realizar operaciones bancarias
    cuenta1.consultar_saldo()
    cuenta1.depositar(500)
    cuenta1.retirar(300)
    cuenta1.retirar(1500)  # Intento de retiro con fondos insuficientes
    cuenta1.consultar_saldo()

    # Eliminar la cuenta y la persona manualmente
    del cuenta1
    del persona1

    # Fin del programa
    print("[INFO] Fin del programa. Destructores automáticos en acción para objetos restantes.")
