print("* Reto2 ")
alto = float(input())
ancho = float(input())
profundo = float(input())
volumen = alto*ancho*profundo
costo = volumen*5

if alto>30:
    costo = costo + 2000
if costo>10000:
    costo = costo + (costo*0.19)

print(volumen)
print(costo)



print(100/19)

'''
* Reto2 
6
8
9
432.0
2160.0
5.2631578947368425
'''