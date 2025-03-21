#funciones
#def nombre de la funcion (parametros)
def saludar (nombre):
    print(f"hola{nombre}")

#llamo la funcion y le paso el parametro
saludar("juan")
saludar("ivan")

#funcion sumar
def sumar(a,b):
    resultado=a+b
    return resultado

numero1= int(input("ingrese el primer numero"))
numero2= int(input("ingrese el segundo numero"))

resultado=sumar(numero1,numero2)
print(resultado)
    