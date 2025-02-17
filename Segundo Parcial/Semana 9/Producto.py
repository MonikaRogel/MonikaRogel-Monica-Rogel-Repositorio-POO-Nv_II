class Producto:
    """
    Semana S9 Monica Rogel
    Clase que representa un producto en el inventario.
    """

    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        :param id: Identificador único del producto (entero).
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible del producto (entero positivo).
        :param precio: Precio del producto (número positivo).
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        """Obtiene el ID del producto."""
        return self.id

    def get_nombre(self):
        """Obtiene el nombre del producto."""
        return self.nombre

    def get_cantidad(self):
        """Obtiene la cantidad disponible del producto."""
        return self.cantidad

    def get_precio(self):
        """Obtiene el precio del producto."""
        return self.precio

    def set_nombre(self, nombre):
        """Actualiza el nombre del producto."""
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        """Actualiza la cantidad disponible del producto."""
        self.cantidad = cantidad

    def set_precio(self, precio):
        """Actualiza el precio del producto."""
        self.precio = precio

    def __str__(self):
        """Representación en cadena del producto."""
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


class Inventario:
    """
    Clase que representa el inventario de la tienda.
    """

    def __init__(self):
        """Constructor de la clase Inventario."""
        self.productos = []

    def añadir_producto(self, id, nombre, cantidad, precio):
        """
        Añade un nuevo producto al inventario.

        :param id: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible del producto.
        :param precio: Precio del producto.
        """
        # Verifica si el ID ya existe en el inventario
        if any(producto.get_id() == id for producto in self.productos):
            print("Error: El ID ya existe en el inventario.")
            return False

        # Verifica que el nombre no esté vacío
        if not nombre or not isinstance(nombre, str):
            print("Error: El nombre del producto no puede estar vacío.")
            return False

        # Verifica que la cantidad sea un número entero positivo
        if not isinstance(cantidad, int) or cantidad < 0:
            print("Error: La cantidad debe ser un número entero positivo.")
            return False

        # Verifica que el precio sea un número positivo
        if not isinstance(precio, (int, float)) or precio < 0:
            print("Error: El precio debe ser un número positivo.")
            return False

        # Si todo está bien, añade el producto
        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto añadido con éxito.")
        return True

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.

        :param id: Identificador único del producto a eliminar.
        """
        producto = next((p for p in self.productos if p.get_id() == id), None)
        if producto:
            self.productos.remove(producto)
            print("Producto eliminado con éxito.")
        else:
            print("Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, nombre=None, cantidad=None, precio=None):
        """
        Actualiza el nombre, la cantidad o el precio de un producto por su ID.

        :param id: Identificador único del producto a actualizar.
        :param nombre: Nuevo nombre del producto (opcional).
        :param cantidad: Nueva cantidad del producto (opcional).
        :param precio: Nuevo precio del producto (opcional).
        """
        producto = next((p for p in self.productos if p.get_id() == id), None)
        if producto:
            if nombre is not None:
                if not nombre or not isinstance(nombre, str):
                    print("Error: El nombre del producto no puede estar vacío.")
                else:
                    producto.set_nombre(nombre)
                    print("Nombre actualizado con éxito.")
            if cantidad is not None:
                if not isinstance(cantidad, int) or cantidad < 0:
                    print("Error: La cantidad debe ser un número entero positivo.")
                else:
                    producto.set_cantidad(cantidad)
                    print("Cantidad actualizada con éxito.")
            if precio is not None:
                if not isinstance(precio, (int, float)) or precio < 0:
                    print("Error: El precio debe ser un número positivo.")
                else:
                    producto.set_precio(precio)
                    print("Precio actualizado con éxito.")
        else:
            print("Error: No se encontró un producto con ese ID.")

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca productos por nombre (insensible a mayúsculas/minúsculas).

        :param nombre: Nombre del producto a buscar.
        :return: Lista de productos que coinciden con el nombre.
        """
        productos_encontrados = [
            p for p in self.productos if nombre.lower() in p.get_nombre().lower()
        ]
        return productos_encontrados

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario ---")
            for producto in self.productos:
                print(producto)
            print("------------------")


class SistemaDeGestionDeInventarios:
    """
    Clase principal que maneja el sistema de gestión de inventarios.
    """

    def __init__(self):
        """Constructor de la clase SistemaDeGestionDeInventarios."""
        self.inventario = Inventario()

    def mostrar_menu(self):
        """Muestra el menú de opciones en la consola."""
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Salir")

    def ejecutar(self):
        """Función principal que maneja la interfaz de usuario."""
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                try:
                    id = int(input("Ingrese el ID del producto (número entero): "))
                    nombre = input("Ingrese el nombre del producto: ")
                    cantidad = int(input("Ingrese la cantidad del producto (entero positivo): "))
                    precio = float(input("Ingrese el precio del producto (número positivo): "))
                    self.inventario.añadir_producto(id, nombre, cantidad, precio)
                except ValueError:
                    print("Error: Entrada inválida. Asegúrese de ingresar números correctos.")

            elif opcion == "2":
                try:
                    id = int(input("Ingrese el ID del producto a eliminar: "))
                    self.inventario.eliminar_producto(id)
                except ValueError:
                    print("Error: El ID debe ser un número entero.")

            elif opcion == "3":
                try:
                    id = int(input("Ingrese el ID del producto a actualizar: "))
                    nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
                    cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
                    precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
                    nombre = nombre if nombre else None
                    cantidad = int(cantidad) if cantidad else None
                    precio = float(precio) if precio else None
                    self.inventario.actualizar_producto(id, nombre, cantidad, precio)
                except ValueError:
                    print("Error: Entrada inválida. Asegúrese de ingresar números correctos.")

            elif opcion == "4":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                productos = self.inventario.buscar_producto_por_nombre(nombre)
                if productos:
                    for producto in productos:
                        print(producto)
                else:
                    print("No se encontraron productos con ese nombre.")

            elif opcion == "5":
                self.inventario.mostrar_inventario()

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaDeGestionDeInventarios()
    sistema.ejecutar()