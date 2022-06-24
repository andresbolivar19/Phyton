
#ciclo while
cantidad =int(0)
iterador = int(1)
cantTanques = int(input())

""" while iterador<= cantTanques:
    largo = float(input())
    if 2.20<=largo<=2.45:
        cantidad +=1
    iterador +=1
print(cantidad) """

CANTIDAD=int(0)
#ciclo for
for i in range(1,cantTanques+1,1):
    LARGO =float(input())
    
    if 2.20<=LARGO<=2.45:
        CANTIDAD +=1
print(CANTIDAD)        