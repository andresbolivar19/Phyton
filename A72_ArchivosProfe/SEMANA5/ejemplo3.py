#conjuntos
#set()
#caracteristicas
#1. Es una coleccion desordenada
#2. No tiene un index (indice), los datos no tienen una posicion fija
#3. No permite datos duplicados, los omite
#4. Es inmutable, no se pueden cambiar los datos, pero los puedo eliminar y agregar nuevos datos

conjunto = set(("mora","banano","cereza","guayaba","mango","fresa")) #conjunto vacio, el par de llaves vacias{} por
#defecto python lo toma como un diccionario vacio
print(conjunto)

#iterar un conjunto solo se puede con for
for x in conjunto:
    print(x)

#buscar algo en el conjunto usando el in
buscar = str(input())
busqueda = buscar in conjunto #busquedad será un dato bool
if busqueda == True:
    print(buscar,"se encuentra en el conjunto de frutas")
else:
    print(buscar,"no se encuentra en el conjunto de frutas")
    print("desea agregar ",buscar,"al conjunto? responda S/N")
    resultado =str(input())
    resultado = resultado.upper()
    if resultado == "S":
        #agregar un dato al conjunto
        conjunto.add(buscar)
        #conjunto.update({buscar})#es similar al extend de la lista, agrega datos iterables, lista, tupla, conjunto
    else:
        print("no agregó nada al conjunto de frutas")

print(conjunto)

#eliminar datos del conjunto
conjunto.remove("cereza") #si el elemento no se encuentra en el conjunto, genera un error
conjunto.discard("pera")#si el elemento no se encuentra, no hace nada
print(conjunto)
delete= conjunto.pop()#eliminar el ultimo dato del conjunto
print(delete)
print(conjunto)

#union de dos conjuntos, unir el conjunto con conjunto2
conjunto2 = {"uva","sandia","manzanas","fresa","mora"}
print(conjunto2)
print("union de los conjuntos 'conjunto' y 'conjunto2'")
conjunto3 = conjunto.union(conjunto2)

print(conjunto3)
conjunto.update(conjunto2)
print(conjunto)

#interseccion de conjuntos
print("interseccion de conjuntos ")
conjunto.intersection_update(conjunto2)
print(conjunto)
inter = conjunto.intersection(conjunto2)
print(inter)
#dejar vacio el conjunto
conjunto.clear()
print(conjunto)

