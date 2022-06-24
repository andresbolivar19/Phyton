
#datos de entrada
notaFinal = float(input("Ingrese la nota final: "))
valorColegiatura = int(560000)
valorIva = 1.1 #iva 10%
valorPagar = float(0.0)
if 0<=notaFinal<=5.0:

    if notaFinal>=4.5:
        #descuento =valorColegiatura*0.3
        valorPagar = valorColegiatura*(1-30/100) #*0.7
    else:  
        #valorPagar = valorColegiatura*0.1 + valorColegiatura
        valorPagar = valorColegiatura*valorIva
else:
    print("Ingresó valor de nota por fuera de 0 a 5")
print("El valor a pagar es: ",valorPagar)

print(3e6)