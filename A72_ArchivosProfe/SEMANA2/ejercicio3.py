#ejercicio 3 [-3,27]

#dato de entrada
numeroIntervalo = int(input("Ingrese un numero: "))

#proceso
if numeroIntervalo >=-3 and numeroIntervalo<=27:
    print("El numero ingresado se encuentra en el intervalo")
elif numeroIntervalo<-3:
    print("El numero ingresado es menor a -3")
    print("No se encuentra en el rango [-3 , 27]")
else:
    print("El numero ingresado es mayor a 27")
    print("No se encuentra en el rango [-3 , 27]")      