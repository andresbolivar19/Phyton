#declara variable de tipo string con str()
mensaje = str("Hola mundo misión tic A72 $% / ¡? @ ")
print(mensaje)
print(type(mensaje)) #type funcion con la cual conozco el tipo de dato de una variable
#variables que nunca pueden declarar
#eje 0hola nunca, -mensaje nunca, nunca una variable debe iniciar con un numero o caracter especial (-+/!##$)

#Si puedo hacer es crear variables en mayuscula o minuscula y usando el guion bajo o under score


#declarar variables numericas entera int()
MiPrimeraVariable = int(125)
print(MiPrimeraVariable)
print(type(MiPrimeraVariable))

#declarar variables numerica decimal float()
mi_segunda_variable= float(-2.365)
print(mi_segunda_variable)
print(type(mi_segunda_variable))

suma = MiPrimeraVariable + mi_segunda_variable
print(suma)

datoStr = str("25")
#conversion de variable int a str
suma2 = str(MiPrimeraVariable) + datoStr
print(suma2)

#conversion de variable str a int
suma = MiPrimeraVariable + int(datoStr)
print(suma)

#conversion de variable float a int
suma = MiPrimeraVariable +int(mi_segunda_variable)
print(suma)

#conversion de variable int a float
suma = float(MiPrimeraVariable) + mi_segunda_variable
print(suma)