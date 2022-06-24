#ciclo while (mientras)

#datos de entrada

manzanas = int(input("Ingrese la cantidad de manzanas a agregar en la cesta: "))
contManzanas=0 #contador

print("Se ha iniciado el carrito, hay",contManzanas,"manzanas")
if manzanas>0: #evalua que si ingresó un valor mayor a 0 para agregar manzanas a la cesta y itere el while
    #proceso
    while (contManzanas <manzanas):
        contManzanas +=1
        print("Ahora hay",contManzanas,"manzanas")
    print("Finalizó el ciclo while")    
else: print("Ingresó una cantidad menor o igual a cero.")

####################
#bucles infinitos OJO con la CONDICION DEL WHILE 

i =59 #contador
while i>=0: #no hay un cambio en la variable i y la condicion siempre sera True
   print("restan",i,"segundos")
   i -=0.5 #restando de 2 en 2

#usando break (ruptura) en while

a=1
while a<6:
    print(a)
    a +=1
    if a ==3:
        #break
        print("ingresa al if ")
        continue 
        
    
#print("Finaliza el while aun estando True por el break")

#continue