
#lista en python
dato_v = [10,20,25,35,8555,456] #crea la lista con datos
print(type(dato_v), len(dato_v), dato_v[5])
dato_v.sort()#ordena los datos de la lista de menor a mayor si son numeros, si es texto orden A - Z
print(dato_v)

dato_x= ["hola" , "mundo",15, [45,55]]
dato_x[3]#ingresar a un indice en especifico de la lista, siempre y cuando ese indice exista sino lo es genera error de indice
print(type(dato_x), len(dato_x), dato_x[3])

listaVacia= []#lista vacia
listaVacia.append("A72") #agrega un dato a la lista
listaVacia.append("Misiontic 22")
print(listaVacia)
listaVacia.clear()#deja vacia la lista
print(listaVacia)


milista= list(("peras","manzanas","kiwi","bananos","fresas","peras"))
print(milista)
#eliminar con informacion contenida en la lista, elimina la 1era coincidencia que exista
milista.remove("peras")
print(milista)

#ordenar la lista
milista.sort()
print(milista)

#eliminar por posicion o indice si no indica ningun valor numerico por defecto elimina el ultimo dato
milista.pop()
print(milista)
#insertar datos a la lista en una posicion x, lo que se va a añadir
milista.insert(3,"granadillas")
print(milista)


#acceder a mas de 1 elemento en listas
print(milista[1:3]) #resultado ['fresas', 'kiwi']
print(milista[0:4:2])#resultado ['bananos', 'kiwi']

print(milista[::-2])

#recorrer una lista con un for
for iterador in milista:
    print(iterador)

#agregar varios elementos al final de la lista
milista.extend(["sandia","uvas"])
print(milista)

#SABER SI UN VALOR SE ENCUENTRA EN LISTA, USANDO in
busqueda = "moras" in milista
print(busqueda)

#CARACTERISTICAS DE LAS LISTAS EN PYTHON
#1. PERMITEN DATOS DUPLICADOS
#2. SON MUTABLES, SE PUEDEN MODIFICAR EN TIEMPO EJECUCIÓN
#3. ES UNA COLECCION ORDENADA (LOS DATOS SEAN DEL MISMO TIPO) 