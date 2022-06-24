'''
print("\n\n 1. Calcular las diagonales de un polígono regular de N lados. Ecuancion es: ")

lados = int(input("Ingresar lados del poligono: "))
resultado1= (lados**2 - 3*lados)/2
resultado2= lados * (lados - 3)/2

print("El resultado con la 1ra formula es: ", resultado1)
print("El resultado con la 2da formula es: ", resultado2)


print("\n\n 2. Calcular con la fórmula de Gauss, la suma de N números enteros. Ecuación es:")

numero = int(input("Ingresar numero entero: "))
resultado1= (numero**2 + numero) / 2
resultado2= (numero * (numero + 1)) / 2

print("El resultado con la 1ra formula es: ", resultado1)
print("El resultado con la 2da formula es: ", resultado2)
print("\n\n 3. Realizar las operaciones básicas ingresando dos (2) números como datos de entrada.")

numero1 = float(input("Ingresar 1er numero: "))
numero2 = float(input("Ingresar 2do numero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potenciacion = numero1 ** numero2
residuo = numero1 % numero2



print("La suma es ", suma)
print("La resta es ", resta)
print("La multiplicacion es ", multiplicacion)
print("La division es ", division)
print("La potenciacion es ", potenciacion)
print("La residuo es ", residuo)


print("\n\n 7. Crear un programa, que pida una cantidad de segundos y que escriba cuántas horas, minutos y segundos son")
numero1 = int(input("Ingresar segundos: "))
horas = int(numero1 // 3600)
resto1 = int(numero1 % 3600)
minutos = int(resto1 // 60)
segundos = int(resto1 % 60)

print("El rsultado es Horas - Minutos - Segundos: ", )
print(horas)
print(minutos)
print(segundos)

print(f"{numero1} segundos es igual a {horas} horas, {minutos} minutos y {segundos} segundos ")
'''

print("\n\n 8. Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros")
# Se recuerda que 1 pie son 12 pulgadas y 1 pulgada son 2.54 cm
pies = float(input("Ingrese pies: "))
pulgadas = float(input("Ingrese pulgadas: "))
centimetros  = (pies*12+pulgadas)*2.54
print(f"El equivalente a {pies} pies y {pulgadas} pulgadas en centimetros es: {centimetros}")

pies2 =  (2.54*12) * pies
pulgadas2 = pulgadas * 2.54
centimetros2  = pies2 + pulgadas2
print(f"El equivalente a {pies} pies y {pulgadas} pulgadas en centimetros es: {centimetros2}")

