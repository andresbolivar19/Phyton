
from math import pi,factorial, cos

def funCosSerieTaylor(angulo, cantidadTerminos):
    x = (angulo/180)*3.1415265
    cosX = 0.0

    factor = factorial
    rta = []#la lista vacia
    for n in range(0,cantidadTerminos,1):
        #funcion coseno
        exponente = (2*n)
        numerador = x**exponente
        denominador = factor(exponente)

        cosX = cosX +(-1)**n * (numerador/denominador)
        resultado = "{} 'cos (x)' {} ".format(n+1,cosX)
        rta.append(resultado) #añado valor a la lista
    return rta  
    

angulo =37

cantidadTerminos = 20
print(funCosSerieTaylor(angulo,cantidadTerminos))

#print(funCosSerieTaylor(53,20))
#print(funCosSerieTaylor(90,20))
print(cos((angulo/180)*3.1415265), cos((53/180)*3.1415265),cos((90/180)*3.1415265) )