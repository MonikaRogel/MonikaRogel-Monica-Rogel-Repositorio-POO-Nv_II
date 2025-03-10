"""----Semana 12
Monica Rogel----"""

import json
from datetime import datetime

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.cargar_datos()

    def guardar_datos(self):
        datos = {
            'libros': {isbn: {'titulo': libro['titulo'], 'autor': libro['autor'], 'categoria': libro['categoria'], 'disponible': libro['disponible']}
                       for isbn, libro in self.libros.items()},
            'usuarios': {id_usuario: {'nombre': usuario['nombre'], 'libros_prestados': usuario['libros_prestados']}
                         for id_usuario, usuario in self.usuarios.items()}
        }
        with open('biblioteca.json', 'w') as f:
            json.dump(datos, f, indent=4)

    def cargar_datos(self):
        try:
            with open('biblioteca.json', 'r') as f:
                datos = json.load(f)
                self.libros = datos.get("libros", {})
                self.usuarios = datos.get("usuarios", {})
        except FileNotFoundError:
            pass

    def agregar_libro(self):
        print("\n📖 Agregar un nuevo libro")
        isbn = input("Ingrese ISBN: ")
        titulo = input("Ingrese Título: ")
        autor = input("Ingrese Autor: ")
        categoria = input("Ingrese Categoría: ")

        if isbn in self.libros:
            print("❌ Error: Este libro ya está registrado.")
            return

        self.libros[isbn] = {"titulo": titulo, "autor": autor, "categoria": categoria, "disponible": True}
        self.guardar_datos()
        print(f"✅ Libro '{titulo}' agregado correctamente.")

    def eliminar_libro(self):
        print("\n📖 Eliminar un libro")
        isbn = input("Ingrese ISBN del libro a eliminar: ")

        if isbn not in self.libros:
            print("❌ Error: Libro no encontrado.")
            return

        del self.libros[isbn]
        self.guardar_datos()
        print(f"✅ Libro con ISBN {isbn} eliminado correctamente.")

    def registrar_usuario(self):
        print("\n👤 Registrar un nuevo usuario")
        id_usuario = input("Ingrese ID de usuario: ")
        nombre = input("Ingrese Nombre del usuario: ")

        if id_usuario in self.usuarios:
            print("❌ Error: El usuario ya está registrado.")
            return

        self.usuarios[id_usuario] = {"nombre": nombre, "libros_prestados": []}
        self.guardar_datos()
        print(f"✅ Usuario '{nombre}' registrado correctamente.")

    def eliminar_usuario(self):
        print("\n👤 Eliminar un usuario")
        id_usuario = input("Ingrese ID del usuario a eliminar: ")

        if id_usuario not in self.usuarios:
            print("❌ Error: Usuario no encontrado.")
            return

        del self.usuarios[id_usuario]
        self.guardar_datos()
        print(f"✅ Usuario con ID {id_usuario} eliminado correctamente.")

    def prestar_libro(self):
        print("\n📖 Prestar un libro")
        id_usuario = input("Ingrese ID del usuario: ")
        isbn = input("Ingrese ISBN del libro a prestar: ")

        if id_usuario not in self.usuarios:
            print("❌ Error: Usuario no encontrado.")
            return
        if isbn not in self.libros:
            print("❌ Error: Libro no encontrado.")
            return
        if not self.libros[isbn]["disponible"]:
            print("❌ Error: El libro ya está prestado.")
            return
        if len(self.usuarios[id_usuario]["libros_prestados"]) >= 3:
            print("❌ Error: El usuario alcanzó el límite de préstamos.")
            return

        self.libros[isbn]["disponible"] = False
        self.usuarios[id_usuario]["libros_prestados"].append({"isbn": isbn, "fecha_prestamo": datetime.now().strftime("%Y-%m-%d")})
        self.guardar_datos()
        print(f"📖 Libro '{self.libros[isbn]['titulo']}' prestado a {self.usuarios[id_usuario]['nombre']}.")

    def devolver_libro(self):
        print("\n📖 Devolver un libro")
        id_usuario = input("Ingrese ID del usuario: ")
        isbn = input("Ingrese ISBN del libro a devolver: ")

        if id_usuario not in self.usuarios:
            print("❌ Error: Usuario no encontrado.")
            return
        if isbn not in [libro["isbn"] for libro in self.usuarios[id_usuario]["libros_prestados"]]:
            print("❌ Error: El usuario no tiene este libro prestado.")
            return

        self.usuarios[id_usuario]["libros_prestados"] = [libro for libro in self.usuarios[id_usuario]["libros_prestados"] if libro["isbn"] != isbn]
        self.libros[isbn]["disponible"] = True
        self.guardar_datos()
        print(f"📚 Libro '{self.libros[isbn]['titulo']}' devuelto con éxito.")

    def buscar_libro(self):
        print("\n🔍 Buscar un libro")
        valor = input("Ingrese título, autor o categoría a buscar: ").lower()
        resultados = [libro for libro in self.libros.values() if valor in libro["titulo"].lower() or valor in libro["autor"].lower() or valor in libro["categoria"].lower()]

        if resultados:
            print("\n📚 Resultados de búsqueda:")
            for libro in resultados:
                print(f"📖 {libro['titulo']} - {libro['autor']} ({libro['categoria']})")
        else:
            print("🔍 No se encontraron libros.")

    def listar_libros_prestados(self):
        print("\n📚 Libros actualmente prestados")
        for id_usuario, usuario in self.usuarios.items():
            if usuario["libros_prestados"]:
                print(f"\n👤 {usuario['nombre']} (ID: {id_usuario}):")
                for libro in usuario["libros_prestados"]:
                    print(f"📖 {libro['isbn']} - Prestado el {libro['fecha_prestamo']}")

    def menu(self):
        while True:
            print("\n📚 GESTIÓN DE BIBLIOTECA DIGITAL")
            print("1. Agregar libro")
            print("2. Eliminar libro")
            print("3. Registrar usuario")
            print("4. Eliminar usuario")
            print("5. Prestar libro")
            print("6. Devolver libro")
            print("7. Buscar libro")
            print("8. Listar libros prestados")
            print("9. Salir")

            opcion = input("-->>Selecione: ")

            funciones = {
                "1": self.agregar_libro,
                "2": self.eliminar_libro,
                "3": self.registrar_usuario,
                "4": self.eliminar_usuario,
                "5": self.prestar_libro,
                "6": self.devolver_libro,
                "7": self.buscar_libro,
                "8": self.listar_libros_prestados,
                "9": lambda: print("📖 Saliendo del sistema. ¡Hasta pronto!") or exit()
            }

            funcion = funciones.get(opcion)
            if funcion:
                funcion()
            else:
                print("❌ Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    Biblioteca().menu()
