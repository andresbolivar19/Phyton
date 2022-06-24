#datos entrada
alto = float(input())
ancho = float(input())
profundo = float(input())

#proceso
volumen =alto*ancho*profundo
costo = volumen*5
#reto2
if alto>30 :
    costo = costo+2000
    #costo += 2000
if costo>10000:
    costo = (costo*0.19)+costo
    #costo *=1.19
#datos de salida
print(volumen)
print(costo)