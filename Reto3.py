from posixpath import split
from re import search


print("* Reto3 ")

numeropaquetes = int(input())
costototal = 0
for i in range(numeropaquetes):
    alto = float(input())
    ancho = float(input())
    profundo = float(input())
    volumen = alto*ancho*profundo
    costo = volumen*5
    if alto>30:
        costo = costo + 2000
    if costo>10000:
        costo = costo + (costo*0.19)
    costototal = costototal + costo
    print(volumen)
    print(costo)
print(costototal)


#print(100/19)

'''
* Reto2 
6
8
9
432.0
2160.0
5.2631578947368425
'''