

#ejemplo pag 38
#funciones python
#def nombre de la funcion(argumentos o variables opcionales ):
def count_each_character(inputString):
    """
    funcion hace x cosa
    """
    stringLen = len(inputString)
    counterArray = [] #lista vacia
    
    for i in range(0,stringLen,1):
        caracter = inputString[i]
        print(caracter, end=" ")
        contador =0
        for j in range(0,stringLen,1):
            if caracter == inputString[j]:
                contador = contador+1
        counterArray.append(contador)#append agrega informacion a la lista a la ultima posicion

    #secuencia de codigo o instrucciones
    #return opcional
    return counterArray #inputString 

dato = str(input("Ingrese un texto: "))

print(count_each_character(dato))
print(count_each_character("Estamos en clase de python"))