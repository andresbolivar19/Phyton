cadena = str(input())
def materias(cadena):
    for i in range (len(cadena)):
        resultado = cadena.split(',')
        return resultado

def listaFrutas(frutas):
    for i in range(len(frutas)):
        print(frutas[i])

numeros = [2,4,5,8]
def multiplicarNumeros(numeros):
    for i in range (len(numeros)+1):
        if (len(numeros) == 0):
            return 0
        elif (len(numeros) == 1):
            return numeros[0]
        else:
            return numeros[0]*multiplicarNumeros(numeros[1:])
