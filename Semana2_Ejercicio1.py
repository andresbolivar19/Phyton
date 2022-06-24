'''
numero = int(input("Ingrese el numero: "))

if numero == 0:
    print("El número ingresado es Cero: ")
elif numero > 0:
    print("El numero ingresado es Positivo")
else:
    print("El numero ingresado es Negativo")

numero1 = int(input("Ingrese el 1er numero: "))
numero2 = int(input("Ingrese el 2do numero: "))
numero3 = int(input("Ingrese el 3ro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El numero mayor es: {numero1} ")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero mayor es: {numero2} ")
else:
    print(f"El numero mayor es: {numero3} ")

num = int (unput('Introducir número: '))
if num == 100:
    print ('El nuermo es igual a 100')
'''

print("1. Elaborar un programa en lenguaje Python, que permita ingresar 3 valores /"
"tipo entero y los imprima en forma descendente. (mayor a menor)")
n1 = int(input("Ingrese el 1r numero "))
n2 = int(input("Ingrese el 2do numero "))
n3 = int(input("Ingrese el 3ro numero "))

if n1 > n2 and n1 > n3:
    mayor = n1
    if n2 > n3:
        medio = n2
        menor = n3
    else:
        medio = n3
        menor = n2
    print(f" El mayor es: {mayor}")
    print(f" El medio es: {medio}")
    print(f" El menor es: {menor}")
elif n2 > n1 and n2 > n3:
    mayor = n2
    if n1 > n3:
        medio = n1
        menor = n3
    else:
        medio = n3
        menor = n1
    print(f" El mayor es: {mayor}")
    print(f" El medio es: {medio}")
    print(f" El menor es: {menor}")    
elif n3 > n1 and n3 > n2:
    mayor = n3
    if n1 > n2:
        medio = n1
        menor = n2
    else:
        medio = n2
        menor = n1
    print(f" El mayor es: {mayor}")
    print(f" El medio es: {medio}")
    print(f" El menor es: {menor}")  
else:
    print("No se cumple ninguna")
