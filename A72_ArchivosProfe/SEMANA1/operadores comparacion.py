#operador igualdad ==
variable1= int(15)
variable2 = float(6.0)
variable3 =  str("hola mundo")
variable4 = str("HOLA")
print(variable3 != variable4)
print(len(variable3)) #conozco la longitud de una variable
print(variable1 == variable2)

#operador diferencia !=
print(variable2 != variable1)

#operador mayor que >
print(variable1 > variable2)

#operador menor que <
print(variable1 <  variable2)

#operador mayor igual >=
print(variable1 >= variable2)

#operador menor igual <=
print(variable1 <= variable2)

################################
#operadores lógicos and or not

#operador and todas las variables que estén 
# involucradas deben ser True para devolver
#un resultado True, de lo contrario el 
#resultado es False

#and 
print(variable1 > 5 and variable2 >6)
#or 
print(variable1 > 5 or variable2 >6)

resultado = 7-2*(13+5)
print(resultado)

#captura de datos empleando input()
print("Ingrese un número entero:")
numero1 = int(input())

print("Ingrese otro número entero:")
numero2 = int(input())

suma = int(numero1+numero2)
porcentaje = int(suma*0.3)
print(porcentaje)