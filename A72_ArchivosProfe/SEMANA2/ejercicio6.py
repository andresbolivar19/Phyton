#año bisiesto
#dato de entrada
anio = int(input("Ingrese un año: "))

#proceso:
if anio%400==0 or anio%4==0 and anio%100 !=0:
    print(f"Año {anio} ingresado es bisiesto")
    print("{:,.0f}".format(anio))
else:
    print("Año NO es bisiesto",anio)