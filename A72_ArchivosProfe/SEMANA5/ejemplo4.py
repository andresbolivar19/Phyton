#diccionarios
#caracteristicas
#1. coleccion ordenada
#2. modificar los datos
#3. no permite claves duplicadas, son unicas
#4. puede contener cualquier tipo de dato, listas, bool, str, tuplas, numeros, diccionario
#5. se componen de pares clave: valor; separados por comas

mi_informacion = {
'nombre' : 'David',
'apellido' : 'Cortez',
'sobrenombre' : 'DD',
'padres' : ["Marín gomez", "Julián Cortez"],
'edad' : 27,
'genero' : 'masculino',
'estado Civil' : 'Soltero',
'hijos' : 2,
'mascotas' : 'Perro',
'nombres de mascotas' : ["chato"]
}
print(mi_informacion.keys())#los nombres de las claves del  dicc
print(mi_informacion.values())#los  valores de cada clave del dicc
print(mi_informacion.items())#devuelve en una lista y en ella los pares clave valor en una tupla con su respectiva info

#se puede hacer referencia a ellos mediante el nombre de la clave.
print(mi_informacion['estado Civil'])
print(mi_informacion.get('estado Civil'))

#len con diccionario, Imprime el número de elementos en el diccionario:
print(len(mi_informacion))

#cambiar diccionario
#con update 
print("update a estado Civil")
mi_informacion.update({"estado Civil":"casado"})

print(mi_informacion['estado Civil'])

#agregar items al diccinario
mi_informacion["escolaridad"]="Tecnico"
print("item escolaridad agregado")
print(mi_informacion)

#eliminar items
#pop debemos especificar la clave a eliminar
print("elimina con pop")
mi_informacion.pop("estado Civil")
print(mi_informacion)

#popitem El popitem()método elimina el último elemento insertado 
# (en versiones anteriores a la 3.7, en su lugar, se elimina un elemento aleatorio):
print("elimina popitem")
mi_informacion.popitem()
print(mi_informacion)

#del elimina el elemento con el nombre de clave especificado:
print("del de apellido")
del mi_informacion['apellido']

print(mi_informacion)

#iterar un diccionario
print("ciclos for")
#1. Imprima todos los nombres clave en el diccionario, uno por uno:
for x in mi_informacion:
    print(x,end=" ")

print("\nImprime todos los valores en el diccionario, uno por uno:")
#2.Imprime todos los valores en el diccionario, uno por uno:
for x in mi_informacion:
    print(mi_informacion[x])

#3.puede usar el values()método para devolver valores de un diccionario:
print("puede usar el values()método para devolver valores de un diccionario:")
for x in mi_informacion.values():
    print(x,end=" ")
#4. Puede usar el keys()método para devolver las claves de un diccionario:

for c in mi_informacion.keys():
    print(c,end=" ")

#5.Recorra las claves y los valores usando el items()método:
print("\nitems")
for x,y in mi_informacion.items():
    print(x, "=",y)

#dejar vacio el diccionario
#clear
#mi_informacion.clear()
print(mi_informacion)

#diccionario vacio
materias = {}
materias["lunes"] = ["fisica","quimica"]
materias["martes"] = ["lenguaje","matematicas"]
materias["miercoles"] = ["ingles"]

datos = str(input("ingrese las materias ")) 
lista =[]
lista.append(datos) 
materias["jueves"] = lista
print(materias)

#mejorar la impresion del diccionario
"""
Dentro del módulo json de Python, hay una función llamada dumps(), 
que convierte un objeto Python en una cadena JSON. Además de la conversión,
también formatea el diccionario en un formato JSON bonito, por lo que puede 
una forma viable de imprimir un diccionario convirtiéndolo primero en JSON.
La función dumps() acepta 3 parámetros utilizados para la impresión bonita: 
el objeto a convertir, un valor booleano sort_keys, que determina si las 
entradas deben ser ordenadas por clave, y indent, que especifica el número 
espacios para la sangría.
"""
#saque sus propias conclusiones
import json
dct_arr = [
  {'Name': 'John', 'Age': '23', 'Country': 'USA'},
  {'Name': 'Jose', 'Age': '44', 'Country': 'Spain'},
  {'Name': 'Anne', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Lee', 'Age': '35', 'Country': 'Japan'}
]
print(json.dumps(dct_arr, sort_keys=False, indent=4))

print(json.dumps(materias,sort_keys=True,indent=3))
print(json.dumps(materias,sort_keys=False,indent=3))

print(json.dumps(mi_informacion,sort_keys=True,indent=4))
#saque sus propias conclusiones de los ultimos 4 print