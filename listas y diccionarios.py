lista=[1,3,50,31]
lista.append(8)
print(lista)

#borrar un elemento
del lista[1] 

#moddificar un valor
lista[0]=3 

#Diccionario
personas={ 
     "persona1": {"nombre":"juan",
                "edad":30,
                "ciudad":"Madrid"},
     "persona2": {"nombre":"maria",
                   "edad":30,
                   "ciudad":"Barcelona"
                   }}

print(personas["persona1"])
datos=personas["persona1"]
print(datos)

print(personas["persona2"])
datos=personas["persona2"]
print(datos)
print(datos["ciudad"])