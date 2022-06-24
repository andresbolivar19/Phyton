#ejericio 1
#dato entrada
'''
ladosPoligono = int(input("Escriba el número\
 de lados:\n"))

#proceso
ecuacion = int((ladosPoligono**2-3*ladosPoligono)/2)

#salida
print("La cantidad de diagonales es: ",ecuacion)
print("El núm de diagonales de {} lados son {}"
.format(ladosPoligono,ecuacion))

#ejercicio 2
#dato entrada
cantN = int(input("Hasta qué núm quiere sumar?:\n"))
#proceso
ecuaGauss = int(((cantN*(cantN+1)))/2)
#salida
print(ecuaGauss)

#ejercicio3
#dato entrada
numero1 = float(input("Ingrese el valor 1:"))
numero2 = float(input("Ingrese el valor 2:"))
#proceso
suma = numero1+numero2
resta = numero2-numero1
multiplicar = numero1*numero2
dividir= numero2/numero1
potencia = numero1**numero2
modulo= numero1%numero2
#salida
print(suma)
print(resta)
print(multiplicar)
print(dividir)
print(potencia)
print(modulo)

#ejercicio4
#dato entrada
baseTrianguloR = float(input("Ingrese la base del triangulo:"))
alturaTrianguloR = float(input("Ingrese la altura del triangulo:"))

ladoAtri = int(input("Escriba el lado A del triangulo: "))
ladoBTri = int(input("Escriba el lado B del triangulo: "))
ladoCTri = int(input("Escriba el lado C del triangulo: "))

baseRectangulo = float(input("Base del rectangulo: "))
alturaRectangulo = float(input("Altura del rectangulo: "))

valorPI = float(3.1415)
radio = int(input("Ingrese el radio del circulo: "))

ladoC = int(input("Escriba un lado del cuadrado: "))

cateto = float(input("Ingrese el valor del cateto del triangulo: "))
#proceso
areaTR = (baseTrianguloR*alturaRectangulo)/2
perimetroTR = ladoAtri+ladoBTri+ladoCTri

areaR = baseRectangulo*alturaRectangulo
perimetroR = 2*baseRectangulo+2*alturaRectangulo

areaC = valorPI*radio**2
perimetroC = 2*valorPI*radio

areaCuadrado = ladoC**2
perimetroCuadrado = 4*ladoC

areaTE =((cateto**2)*3**0.5)/4
#salida
print(areaTR)
print(perimetroTR)
print(areaR)
print(perimetroR)
print(areaC)
print(perimetroC)
print(areaCuadrado)
print(perimetroCuadrado)
print(areaTE)

#ejercicio5
#dato entrada
celsius = int(input("Escriba la temperatura en celsius: "))
#proceso
fahrenheit = 1.8*celsius+32
#salida
print(fahrenheit)

#ejercicio6
#dato entrada
FAHRENHEIT = int(input("Ingrese la temperatura en °F: "))
#proceso
CELSIUS = (FAHRENHEIT-32)/1.8
CELSIUS = round(CELSIUS,3) #round redondeo numeros con decimales
#salida
print(CELSIUS)

#ejercicio7
#dato entrada
segundos = int(input("Ingrese una cantidad de segundos: "))
#proceso
horas = int(segundos//3600)
resto1 = segundos%3600
minutos = int(resto1//60)
segundos1 = resto1%60
#salida
print(f"{segundos} seg son {horas} H, {minutos}\
 mm y {segundos1} ss")

#ejercicio8
#dato entrada
meses = int(input("Escriba X meses: "))
#proceso
anios = meses/12
anios = round(anios,2)
#salida
print(anios)

#ejercicio9
#dato entrada
salarioMes = float(input())
diasTrabajados= int(input())
#proceso
cesantias = (salarioMes*diasTrabajados)/360
intereses= (cesantias*diasTrabajados*0.12)/360
#salida
print(cesantias)
print(intereses)

#ejercicio10
#dato entrada
numero1 = float(input("Escriba el numero 1: "))
numero2 = float(input("Escriba el numero 2: "))
#proceso
mediaArit = (numero1+numero2)/2
#salida
print(mediaArit)

#ejercicio11
#dato entrada
pies = int(input("Ingrese la cantidad de pies: "))
pulgadas = int(input("Ingrese la cantidad de pulgadas: "))
#proceso
centimetros = (pies*12+pulgadas)*2.54
#salida
print(f"{pies} pies y {pulgadas} pulgadas son {centimetros} cm")

#ejercicio12
#dato entrada
peso = float(input("Cuanto es su peso en kg: "))
altura = float(input("Cuanto es su estatura en m: "))
#proceso
imc = peso/altura**2
imc = round(imc,3)
#salida
print(imc)

#ejercicio13
#dato entrada
masa = int(input("Ingrese el valor de la masa en kg: "))
velocidad = int(input("La velocidad en m/s: "))
#proceso
energiaCinetica = int(0.5*masa*velocidad**2)
#salida
print(energiaCinetica)

#ejercicio14
#dato entrada
horasTrabajadas = int(input("Cuantas horas laboro al mes: "))
#proceso
valorHora = 37000
SALARIO = horasTrabajadas*valorHora

gastoAdmin = SALARIO*0.05#5/100
fondoSolidario = SALARIO*0.125 #12.5/100
arl = SALARIO*0.035 #3.5/100

descuentos = int(gastoAdmin+fondoSolidario+arl)
salarioNeto = SALARIO-descuentos
#salida
print(SALARIO)
print(descuentos)
print(salarioNeto)

#ejercicio15
#dato entrada
R1 = int(input())
R2 = int(input())
R3 = int(input())
#proceso
RE = 1/((1/R1)+(1/R2)+(1/R3))
RE = round(RE,2)
#salida
print(RE)
'''
#ejercicio16
#dato entrada
miSalario = int(input("Su salario es : "))
#proceso
alimentos = miSalario*0.2
pasajes = miSalario*0.15
boletos = miSalario*0.1
libros = miSalario*0.15
arriendo = miSalario*0.4
#salida
print(alimentos)
print(pasajes)
print(boletos)
print(libros)
print(arriendo)