
from math import pi,factorial, sin

def funSenoSerieTaylor(angulo, cantidadTerminos):
    x = (angulo/180)*3.1415265
    senx = 0.0

    factor = factorial
    rta = []#la lista vacia
    for n in range(0,cantidadTerminos,1):
        #funcion seno
        exponente = (2*n+1)
        numerador = x**exponente
        denominador = factor(exponente)

        senx = senx +(-1)**n * (numerador/denominador)
        resultado = "{} 'sen (x)' {} ".format(n+1,senx)
        rta.append(resultado) #añado valor a la lista
    return rta #(i+1, 'senx ', senx)
    

angulo =37

cantidadTerminos = 20
print(funSenoSerieTaylor(angulo,cantidadTerminos))

#print(funSenoSerieTaylor(53,20))
#print(funSenoSerieTaylor(90,20))
print(sin((angulo/180)*3.1415265), sin((53/180)*3.1415265),sin((90/180)*3.1415265) )