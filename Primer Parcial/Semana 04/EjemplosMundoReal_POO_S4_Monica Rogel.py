# EjemplosMundoReal_POO-Semana 04 Monica Rogel

# Simulador_bancario_MonykR

from abc import ABC, abstractmethod

# Clase abstracta base para las cuentas
# Representa el modelo general para cualquier tipo de cuenta bancaria.
# Contiene métodos comunes como depositar y retirar, y declara métodos abstractos
# que deben ser implementados por las subclases.
class CuentaBancaria(ABC):
    def __init__(self, titular: str, saldo_inicial: float):
        """
        Inicializa una cuenta bancaria con un titular y un saldo inicial.

        :param titular: Nombre del titular de la cuenta.
        :param saldo_inicial: Monto inicial depositado en la cuenta.
        """
        self.titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        """
        Devuelve el saldo actual de la cuenta.
        """
        return self._saldo

    def depositar(self, monto: float):
        """
        Agrega dinero a la cuenta, siempre que el monto sea positivo.

        :param monto: Cantidad de dinero a depositar.
        """
        if monto > 0:
            self._saldo += monto
            print(f"Se han depositado ${monto:.2f} a la cuenta de {self.titular}.")
        else:
            print("El monto a depositar debe ser positivo.")

    @abstractmethod
    def retirar(self, monto: float):
        """
        Método abstracto para retirar dinero. Debe ser implementado por las subclases.
        """
        pass

    @abstractmethod
    def mostrar_detalles(self):
        """
        Método abstracto para mostrar los detalles de la cuenta. Debe ser implementado por las subclases.
        """
        pass


# Subclase para cuentas de ahorro
# Representa una cuenta de ahorro con una tasa de interés.
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular: str, saldo_inicial: float, tasa_interes: float):
        """
        Inicializa una cuenta de ahorro con un titular, saldo inicial y tasa de interés.

        :param titular: Nombre del titular de la cuenta.
        :param saldo_inicial: Monto inicial depositado en la cuenta.
        :param tasa_interes: Porcentaje de interés aplicado al saldo (por ejemplo, 0.02 para un 2%).
        """
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes

    def calcular_interes(self):
        """
        Calcula los intereses generados por el saldo actual.

        :return: Monto de intereses generados.
        """
        interes = self._saldo * self.tasa_interes
        return interes

    def retirar(self, monto: float):
        """
        Retira dinero de la cuenta si el saldo es suficiente.

        :param monto: Cantidad de dinero a retirar.
        """
        if monto > 0 and monto <= self._saldo:
            self._saldo -= monto
            print(f"Se han retirado ${monto:.2f} de la cuenta de ahorro de {self.titular}.")
        else:
            print("Monto no válido o fondos insuficientes en la cuenta de ahorro.")

    def mostrar_detalles(self):
        """
        Muestra los detalles de la cuenta de ahorro.
        """
        print(f"Cuenta de Ahorro de {self.titular}. Saldo: ${self.saldo:.2f}. Tasa de interés: {self.tasa_interes * 100:.2f}%")


# Subclase para cuentas corrientes
# Representa una cuenta corriente con la posibilidad de sobregiro.
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular: str, saldo_inicial: float, sobregiro_maximo: float):
        """
        Inicializa una cuenta corriente con un titular, saldo inicial y un límite de sobregiro.

        :param titular: Nombre del titular de la cuenta.
        :param saldo_inicial: Monto inicial depositado en la cuenta.
        :param sobregiro_maximo: Monto máximo permitido para sobregiro.
        """
        super().__init__(titular, saldo_inicial)
        self.sobregiro_maximo = sobregiro_maximo

    def retirar(self, monto: float):
        """
        Retira dinero de la cuenta, permitiendo sobregiro hasta el límite especificado.

        :param monto: Cantidad de dinero a retirar.
        """
        if monto > 0 and monto <= (self._saldo + self.sobregiro_maximo):
            self._saldo -= monto
            print(f"Se han retirado ${monto:.2f} de la cuenta corriente de {self.titular}.")
        else:
            print("Monto no válido o excede el límite de sobregiro en la cuenta corriente.")

    def mostrar_detalles(self):
        """
        Muestra los detalles de la cuenta corriente.
        """
        print(f"Cuenta Corriente de {self.titular}. Saldo: ${self.saldo:.2f}. Sobregiro máximo: ${self.sobregiro_maximo:.2f}")


# Programa principal
# Maneja el menú interactivo para gestionar las cuentas bancarias.
if __name__ == "__main__":
    cuentas = []  # Lista para almacenar las cuentas creadas

    while True:
        print("\n--- Menú del Sistema Bancario ---")
        print("1. Crear una cuenta de ahorro")
        print("2. Crear una cuenta corriente")
        print("3. Ver detalles de una cuenta")
        print("4. Depositar dinero")
        print("5. Retirar dinero")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Crear cuenta de ahorro
            titular = input("Nombre del titular: ")
            saldo_inicial = float(input("Saldo inicial: "))
            tasa_interes = 0.02  # Tasa fija del 2%
            cuenta = CuentaAhorro(titular, saldo_inicial, tasa_interes)
            cuentas.append(cuenta)
            print(f"Cuenta de ahorro creada para {titular} con saldo inicial de ${saldo_inicial:.2f}.")

        elif opcion == "2":
            # Crear cuenta corriente
            titular = input("Nombre del titular: ")
            saldo_inicial = float(input("Saldo inicial: "))
            sobregiro_maximo = 500.0  # Sobregiro fijo de $500
            cuenta = CuentaCorriente(titular, saldo_inicial, sobregiro_maximo)
            cuentas.append(cuenta)
            print(f"Cuenta corriente creada para {titular} con saldo inicial de ${saldo_inicial:.2f}.")

        elif opcion == "3":
            # Mostrar detalles de la cuenta
            titular = input("Nombre del titular: ")
            cuenta = next((c for c in cuentas if c.titular == titular), None)
            if cuenta:
                cuenta.mostrar_detalles()
            else:
                print("No se encontró una cuenta con ese titular.")

        elif opcion == "4":
            # Depositar dinero
            titular = input("Nombre del titular: ")
            monto = float(input("Monto a depositar: "))
            cuenta = next((c for c in cuentas if c.titular == titular), None)
            if cuenta:
                cuenta.depositar(monto)
            else:
                print("No se encontró una cuenta con ese titular.")

        elif opcion == "5":
            # Retirar dinero
            titular = input("Nombre del titular: ")
            tipo_cuenta = input("¿De qué tipo de cuenta desea retirar? (ahorro/corriente): ").strip().lower()
            monto = float(input("Monto a retirar: "))
            cuenta = next((c for c in cuentas if c.titular == titular and
                           ((tipo_cuenta == "ahorro" and isinstance(c, CuentaAhorro)) or
                            (tipo_cuenta == "corriente" and isinstance(c, CuentaCorriente)))), None)
            if cuenta:
                cuenta.retirar(monto)
                print(f"Saldo restante en la cuenta de {tipo_cuenta}: ${cuenta.saldo:.2f}")
            else:
                print(f"No se encontró una cuenta de tipo {tipo_cuenta} para el titular {titular}.")

        elif opcion == "6":
            # Salir del programa
            print("Saliendo del sistema bancario. ¡Gracias por usarlo!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")
