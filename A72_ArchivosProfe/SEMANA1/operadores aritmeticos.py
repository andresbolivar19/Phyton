# suma +
dato1 = int(15)
dato2 = float(2.9854)
suma = dato1+dato2
print(suma)
print(type(suma))
#redondeo de decimales con round
#suma = round(suma,2)
#print(suma)
 
#Formateo de cadena de texto strin
print("El resultado de %d + %f= %.2f "%(dato1,dato2, suma))
print("Rta {} + {}= {:.3f}".format(dato1,dato2,suma))
print(f"{dato1} + {dato2} = {suma}")

#resta -
resta= dato1-dato2
print(resta)
str1 ="14"
str2="25"
#resta = str1-str2
#print(resta)

#multiplicacion *
multiplicacion = dato1*dato2
print(multiplicacion)

#division /
division = dato1/dato2

print(division)
print(type(division))
division = dato2/dato1
print(division)

#division entera //
divisionEntera = dato1//dato2
print(divisionEntera)
print(type(divisionEntera))

#potenciacion **
potencia = dato1**3 #(15)^3
print(potencia)

#modulo o residuo de la division %
modulo = dato1%dato2
print(modulo)