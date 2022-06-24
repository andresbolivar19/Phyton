
#dato de entrada
valorVehiculo = float(input("Ingrese el valor de vehiculo:"))
#proceso
impuesto = float(0.0)
if valorVehiculo >=0:
    if valorVehiculo<=50950000:
        impuesto = valorVehiculo*0.015 #1.5/100
        print("El valor a pagar es")
    elif 50950000<valorVehiculo<=114640000:
        impuesto = valorVehiculo*0.025
        print("El valor a pagar es:")
    
    else:
        impuesto = valorVehiculo*0.035
        print("El valor a pagar es $")

else:
    print("Ingresó un valor incorrecto.")

print("{:,.2f}".format(impuesto))#mostrar el valor comas de miles 2,000,000.00

#otra alternativa

if valorVehiculo >=0:
    if valorVehiculo<=50950000:
        impuesto = valorVehiculo*0.015 #1.5/100
        print("$$  es")
    elif valorVehiculo<=114640000:
        impuesto = valorVehiculo*0.025
        print("$$$ es:")
    
    else:
        impuesto = valorVehiculo*0.035
        print(" $")

else:
    print("Ingresó un valor incorrecto.")

print(impuesto)