"""
📌 SISTEMA DE GESTIÓN DE INVENTARIOS MEJORADO
📆 Semana 10 - Programación en Python
👩‍💻 Desarrollado por: Mónica Rogel

🔹 Este sistema permite gestionar un inventario de productos.
🔹 📦 El inventario **YA VIENE CON PRODUCTOS PREVIAMENTE CARGADOS**.
🔹 📂 Si el archivo de inventario no existe, se crea automáticamente con productos iniciales.
"""

import json
import os


class Producto:
    """🛒 Clase que representa un producto en el inventario."""

    def __init__(self, id, nombre, cantidad, precio):
        """Constructor de la clase Producto."""
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        """Convierte un producto en un diccionario para almacenarlo en JSON."""
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    def __str__(self):
        """Representación en texto del producto."""
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    """📦 Clase que gestiona el inventario de productos."""

    ARCHIVO = "inventario.txt"

    PRODUCTOS_PREDETERMINADOS = [
        {"id": 1, "nombre": "Manzanas", "cantidad": 50, "precio": 0.5},
        {"id": 2, "nombre": "Naranjas", "cantidad": 30, "precio": 0.8},
        {"id": 3, "nombre": "Plátanos", "cantidad": 40, "precio": 0.6},
        {"id": 4, "nombre": "Leche", "cantidad": 20, "precio": 1.2},
        {"id": 5, "nombre": "Huevos", "cantidad": 12, "precio": 2.5}
    ]

    def __init__(self):
        """Inicializa el inventario cargando datos desde el archivo."""
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo o usa productos predeterminados si no existe."""
        if not os.path.exists(self.ARCHIVO):
            print("📂 Archivo de inventario no encontrado. Creando con productos predeterminados...")
            self.productos = [Producto(**prod) for prod in self.PRODUCTOS_PREDETERMINADOS]
            self.guardar_inventario()
            return

        try:
            with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                contenido = f.read().strip()
                if contenido:
                    datos = json.loads(contenido)
                    self.productos = [Producto(**prod) for prod in datos]
                    print("✅ Inventario cargado correctamente. (Productos iniciales incluidos)")
                else:
                    print("⚠️ Archivo vacío. Se usará el inventario predeterminado.")
                    self.productos = [Producto(**prod) for prod in self.PRODUCTOS_PREDETERMINADOS]
                    self.guardar_inventario()
        except (json.JSONDecodeError, FileNotFoundError):
            print("⚠️ Error: Archivo corrupto. Restaurando inventario predeterminado...")
            self.productos = [Producto(**prod) for prod in self.PRODUCTOS_PREDETERMINADOS]
            self.guardar_inventario()

    def guardar_inventario(self):
        """Guarda los productos en un archivo JSON."""
        try:
            with open(self.ARCHIVO, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4)
            print("✅ Inventario guardado con éxito.")
        except PermissionError:
            print("⛔ Error: No se puede escribir en el archivo.")

    def mostrar_inventario(self):
        """📜 Muestra los productos del inventario."""
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📜 INVENTARIO ACTUAL:")
            for p in self.productos:
                print(p)
            print("------------------")

    def eliminar_producto(self, id):
        """🗑️ Elimina un producto del inventario."""
        for i, producto in enumerate(self.productos):
            if producto.id == id:
                del self.productos[i]
                self.guardar_inventario()
                print("✅ Producto eliminado con éxito.")
                return
        print("⚠️ Error: Producto no encontrado.")


class SistemaDeGestionDeInventarios:
    """🏪 Sistema interactivo de gestión de inventarios."""

    def __init__(self):
        self.inventario = Inventario()

    def solicitar_entero(self, mensaje):
        """Solicita un número entero y maneja errores."""
        while True:
            try:
                valor = input(mensaje)
                if valor.strip() == "":
                    return None
                valor = int(valor)
                if valor < 0:
                    print("⚠️ Error: Ingrese un número entero positivo.")
                else:
                    return valor
            except ValueError:
                print("⚠️ Error: Ingrese un número válido.")

    def solicitar_decimal(self, mensaje):
        """Solicita un número decimal y maneja errores."""
        while True:
            try:
                valor = input(mensaje)
                if valor.strip() == "":
                    return None
                valor = float(valor)
                if valor < 0:
                    print("⚠️ Error: Ingrese un número positivo.")
                else:
                    return valor
            except ValueError:
                print("⚠️ Error: Ingrese un número válido.")

    def mostrar_menu(self):
        """📌 Muestra el menú de opciones."""
        print("\n📌 MENÚ DEL INVENTARIO:")
        print("1️⃣  Mostrar inventario")
        print("2️⃣  Agregar producto")
        print("3️⃣  Actualizar producto")
        print("4️⃣  Eliminar producto")
        print("5️⃣  Salir")

    def ejecutar(self):
        """Ejecuta el sistema de gestión de inventarios."""
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.inventario.mostrar_inventario()

            elif opcion == "2":
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = self.solicitar_entero("Ingrese la cantidad: ")
                precio = self.solicitar_decimal("Ingrese el precio: ")
                self.inventario.productos.append(Producto(len(self.inventario.productos) + 1, nombre, cantidad, precio))
                self.inventario.guardar_inventario()
                print(f"✅ Producto '{nombre}' agregado correctamente.")

            elif opcion == "3":
                id = self.solicitar_entero("Ingrese el ID del producto a actualizar: ")
                nombre = input("Nuevo nombre (deje en blanco para no cambiar): ") or None
                cantidad = self.solicitar_entero("Nueva cantidad (deje en blanco para no cambiar): ")
                precio = self.solicitar_decimal("Nuevo precio (deje en blanco para no cambiar): ")
                self.inventario.guardar_inventario()
                print("✅ Producto actualizado con éxito.")

            elif opcion == "4":
                id = self.solicitar_entero("Ingrese el ID del producto a eliminar: ")
                self.inventario.eliminar_producto(id)

            elif opcion == "5":
                print("🔚 Saliendo del sistema...")
                break

            else:
                print("⚠️ Opción no válida.")


if __name__ == "__main__":
    print("\n🔹 **BIENVENIDO AL SISTEMA DE INVENTARIO MEJORADO** 🔹")
    print("📂 El inventario ya viene con productos precargados.")
    sistema = SistemaDeGestionDeInventarios()
    sistema.ejecutar()
