estudiantes = {
"Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},

    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},

    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}


def agregar_estudiante():
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad del estudiante: "))
    materias = input("Materias aprobadas (separadas por coma): ").split(", ")
    estudiantes[nombre] = {"edad": edad, "materias": materias}
    print(f"Estudiante {nombre} agregado exitosamente.")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        for nombre, datos in estudiantes.items():
            print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {', '.join(datos['materias'])}")

def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado.")
    else:
        print("El estudiante no existe en la lista.")

def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        datos = estudiantes[nombre]
        print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {', '.join(datos['materias'])}")
    else:
        print("Estudiante no encontrado.")

def buscar_por_palabra():
    palabra = input("Ingrese la palabra clave: ").lower()
    encontrados = [nombre for nombre in estudiantes if palabra in nombre.lower()]
    if encontrados:
        print("Estudiantes encontrados:")
        for nombre in encontrados:
            print(f"- {nombre}")
    else:
        print("No se encontraron coincidencias.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Eliminar estudiante")
        print("4. Buscar estudiante")
        print("5. Buscar por palabra clave")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                agregar_estudiante()
            case "2":
                mostrar_estudiantes()
            case "3":
                eliminar_estudiante()
            case "4":
                buscar_estudiante()
            case "5":
                buscar_por_palabra()
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                    print("Opción no válida, intente de nuevo.")
menu()