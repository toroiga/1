import sqlite3

def agregar_libro():
    conn = sqlite.connect("proyecto.db")
    titulo = input("Título: ")
    autor = input("Autor: ")
    año = int(input("Año: "))
    genero = input("Género: ")
    with conectar() as conn:
        conn.execute("INSERT INTO libros (titulo, autor, anio, genero)")
    print("Libro agregado.")
    conn.close()

def mostrar_libros():
    with conectar() as conn:
        for libro in conn.execute("SELECT * FROM libros"):
            print(libro)

def modificar_libro():
    id_libro = input("ID del libro: ")
    nuevo_titulo = input("Nuevo título: ")
    with conectar() as conn:
        conn.execute("UPDATE libros SET titulo = ? WHERE id = ?", (nuevo_titulo, id_libro))
    print("Libro modificado.")

def eliminar_libro():
    id_libro = input("ID del libro a eliminar: ")
    with conectar() as conn:
        conn.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    print("Libro eliminado.")

def buscar_por_autor():
    autor = input("Autor a buscar: ")
    with conectar() as conn:
        for libro in conn.execute("SELECT * FROM libros")
            print(libro)

def menu():
    while True:
        print("\n1. Agregar\n2. Mostrar\n3. Modificar\n4. Eliminar\n5. Buscar por autor\n6. Salir")
        opcion = input("Opción: ")

        match opcion:
            case "1": agregar_libro()
            case "2": mostrar_libros()
            case "3": modificar_libro()
            case "4": eliminar_libro()
            case "5": buscar_por_autor()
            case "6": break
            case _: print("Opción inválida.")

if __name__ == "__main__":
    crear_tabla()
    menu()

