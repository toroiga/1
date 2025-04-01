alumnos= {"nombre": "",
        "edad": "",
        "materias aprobadas": ""}

print("Bienvenido al Menú")
print("Elija una opcion")
opcion= int(input("1= agregar alumno - 2= mostrar la lista - 3= eliminar un estudiante - 4= buscar un estudiante - 5= verificar una palabra clave"))
match opcion:
    case 1:
        alumnos["nombre"]=input(print("ingrese el nombre del alumno"))
        alumnos["edad"]=int(input(print("ingrese la edad del alumno")))
        alumnos["materias aprobadas"]=input(print("ingrese las materias aprobadas"))
        opcion= int(input("1= agregar alumno - 2= mostrar la lista - 3= eliminar un estudiante - 4= buscar un estudiante - 5= verificar una palabra clave"))

    case 2:
        print(alumnos)
        opcion= int(input("1= agregar alumno - 2= mostrar la lista - 3= eliminar un estudiante - 4= buscar un estudiante - 5= verificar una palabra clave"))

    case 3:
        del alumnos
        opcion= int(input("1= agregar alumno - 2= mostrar la lista - 3= eliminar un estudiante - 4= buscar un estudiante - 5= verificar una palabra clave"))

    case 4:
        nombre=input(print("ingrese el nombre del alumno que busca"))
        if nombre in alumnos:
            print(alumnos[nombre])
        opcion= int(input("1= agregar alumno - 2= mostrar la lista - 3= eliminar un estudiante - 4= buscar un estudiante - 5= verificar una palabra clave"))

    case 5:
        palabra= input(print("ingrese la palabra que desea buscar"))
        if palabra in alumnos:
            print(alumnos[palabra])
        opcion= int(input("1= agregar alumno - 2= mostrar la lista - 3= eliminar un estudiante - 4= buscar un estudiante - 5= verificar una palabra clave"))

    case _: 
        print("seleccione una opcion posible")
        opcion= int(input("1= agregar alumno - 2= mostrar la lista - 3= eliminar un estudiante - 4= buscar un estudiante - 5= verificar una palabra clave"))

