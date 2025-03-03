"""
📌 SISTEMA AVANZADO DE GESTIÓN DE INVENTARIOS
📆 Semana 11 - Fundamentos de colecciones
👩‍💻 Desarrollado por: Mónica Rogel
"""

import json  # Se importa el módulo JSON para manejar el almacenamiento en archivos

# 📌 Clase Producto: Representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en stock
        self.precio = precio  # Precio unitario

    def __str__(self):
        """Devuelve una representación en texto del producto."""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

# 📌 Clase Inventario: Maneja la colección de productos usando un diccionario
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario donde clave = ID y valor = Producto

    def agregar_producto(self, producto):
        """Añade un producto al inventario con confirmación antes de guardar."""
        if producto.id_producto in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"Producto '{producto.nombre}' agregado temporalmente.")

            # Confirmación antes de guardar en archivo
            confirmar = input("¿Desea guardar este producto en el inventario? (s/n): ").strip().lower()
            if confirmar == 's':
                self.guardar_inventario()
                print(f"Producto '{producto.nombre}' guardado permanentemente.")
            else:
                del self.productos[producto.id_producto]  # Se elimina si no se confirma
                print("Operación cancelada. El producto no se ha guardado.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID."""
        if id_producto in self.productos:
            producto_eliminado = self.productos.pop(id_producto)
            print(f"Producto '{producto_eliminado.nombre}' eliminado del inventario.")
            self.guardar_inventario()
        else:
            print("Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        """Actualiza los datos de un producto."""
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nombre:
                producto.nombre = nombre
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"Producto '{producto.nombre}' actualizado.")
            self.guardar_inventario()
        else:
            print("Error: No se encontró un producto con ese ID.")

    def buscar_por_id(self, id_producto):
        """Busca un producto por su ID."""
        producto = self.productos.get(id_producto)
        if producto:
            print("Resultado de la búsqueda:")
            print(producto)
        else:
            print("No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        """Busca productos cuyo nombre contenga la palabra ingresada."""
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            print("\n--- Inventario Actual ---")
            for producto in self.productos.values():
                print(producto)
        else:
            print("\nEl inventario está vacío.")  # Mensaje claro cuando no hay productos

    def guardar_inventario(self, archivo="inventario.json"):
        """Guarda el inventario en un archivo JSON."""
        with open(archivo, 'w') as f:
            inventario_serializado = {
                id_producto: {"nombre": producto.nombre, "cantidad": producto.cantidad, "precio": producto.precio}
                for id_producto, producto in self.productos.items()
            }
            json.dump(inventario_serializado, f)
            print(f"Inventario guardado en '{archivo}'.")

    def cargar_inventario(self, archivo="inventario.json"):
        """Carga el inventario desde un archivo JSON."""
        try:
            with open(archivo, 'r') as f:
                inventario_serializado = json.load(f)
                self.productos = {
                    int(id_producto): Producto(int(id_producto), datos["nombre"], datos["cantidad"], datos["precio"])
                    for id_producto, datos in inventario_serializado.items()
                }
                print(f"Inventario cargado desde '{archivo}'.")
        except FileNotFoundError:
            print("No se encontró el archivo de inventario. Se creará uno nuevo al guardar.")
        except json.JSONDecodeError:
            print("Error al cargar el inventario: archivo corrupto o vacío.")

# 📌 Submenú de búsqueda
def mostrar_submenu_busqueda():
    """Permite elegir el tipo de búsqueda."""
    print("\n--- Tipo de Búsqueda ---")
    print("1. Buscar por ID")
    print("2. Buscar por nombre")
    print("3. Volver al menú principal")

# 📌 Función principal del programa
def main():
    inventario = Inventario()
    inventario.cargar_inventario()  # Cargar inventario al iniciar

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ").strip()
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            nombre = input("Ingrese el nuevo nombre (deje vacío para no cambiar): ").strip() or None
            cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ").strip()
            precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ").strip()

            if cantidad:
                cantidad = int(cantidad)
            if precio:
                precio = float(precio)

            inventario.actualizar_producto(id_producto, nombre, cantidad, precio)

        elif opcion == "4":
            while True:
                mostrar_submenu_busqueda()
                sub_opcion = input("Seleccione una opción de búsqueda: ")
                if sub_opcion == "1":
                    id_producto = int(input("Ingrese el ID del producto a buscar: "))
                    inventario.buscar_por_id(id_producto)
                elif sub_opcion == "2":
                    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
                    inventario.buscar_por_nombre(nombre)
                elif sub_opcion == "3":
                    break

        elif opcion == "5":
            inventario.mostrar_inventario()
            input("\nPresiona ENTER para continuar...")

        elif opcion == "8":
            print("Saliendo del sistema...")
            inventario.guardar_inventario()
            break

if __name__ == "__main__":
    main()
