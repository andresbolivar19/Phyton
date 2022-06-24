#datos de entrada
peso = float(input("Ingrese el peso en Kg: "))
altura = float(input("Ingrese la altura en mt: "))
#proceso
imc = peso/altura**2
imc = round(imc,2)#redondear decimales 2 => mostrar 2 decimales 
#y redondea el 3 si es >5
resultado = str("")
if imc <16 :
    resultado = "Delgadez severa"
elif imc<=16.99: #16<=imc<=16.99:
    resultado = "Delgadez moderada"
elif imc<=18.49:
    resultado = "Delgadez aceptable" 
elif imc <=24.99:
    resultado = "Peso normal"  
elif imc <=29.99:
    resultado = "Sobrepeso"
elif imc<=34.99:
    resultado = "Obesidad tipo 1"
elif imc<=39.99:
    resultado = "Obesidad tipo 2"
elif imc<=49.99:
    resultado = "Obesidad mórbida"    
else:
    resultado = "Obesidad tipo 4 extrema"

#datos de salida
print(resultado,imc)