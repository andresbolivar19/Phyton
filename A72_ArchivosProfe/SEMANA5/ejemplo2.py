
#TUPLAS EN PYTHON 
#CARACTERISTICAS DE LAS TUPLAS
#1. COLECCION ORDENADA
#2. PERMITE VALORES DUPLICADOS
#3. ES INMUTABLE, NO SE PUEDE MODIFICAR EN TIEMPO DE EJECUCION, ELIMINAR, AGREGAR O CAMBIAR ELEMENTOS DESPUES DE CREADA LA TUPLA

mitupla = ()#tupla vacia
print(type(mitupla))

tupla = tuple(("moras","cerezas","guayabas","moras","frambuesas","sandias","naranjas","mandarinas"))
print(tupla)
#ACCEDER A UN INDICE DE LA TUPLA
print(tupla[-1])#obtiene el ultimo elemento de la tupla

#ACCEDER A MAS DE 1 ELEMENTO EN LA TUPLA
print(tupla[-4:-1])#-1 indica la ultima posicion de la tupla
print(tupla[2:]) #inicia desde la posicion 2
print(tupla[:4]) #finaliza hasta la posicion 4 excluyendo ese valor

print(tupla.count("moras"))

#eliminar o agregar informacion a la tupla no tiene metodos para agregar y eliminar valores a la tupla
#1. si desea hacer eliminacion o adicion de info a la tupla debe convertirla a una lista, y 
#posteriormente la vuelve a convertir a una tupla

#iterar tuplas
for i in range(len(tupla)):
    print(tupla[i])
i=0
while i<len(tupla):
    print(tupla[i],end=" ")
    i = i+1