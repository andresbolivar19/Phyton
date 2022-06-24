print("Ejemplo 1: ")
def kms_to_ms(velocity_kms):
    kilometer_in_meter = 1000
    seconds_in_hour = 3600
    velocity_ms = velocity_kms * kilometer_in_meter / seconds_in_hour
    print(velocity_ms)
    #return velocity_ms
kms_to_ms(10)

print("\n\nEjemplo 2: ")
from datetime import datetime
from posixpath import split
def chat(name, msg):
    date = datetime.now()
    print("{}: {}".format(name, msg))
    print(date)
    #return date
chat('Pedro', 'Hola, como estas?')

print("\n\nEjemplo 3: ")
from datetime import datetime
def chat(name, msg = 'Mensaje predeterminado'):
    date = datetime.now()
    print("{}: {}".format(name, msg))
    print(date)
    #return date
chat('Pedro')

print("\n\nEjemplo 4: Factorial ")
def factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ("No existe el factorial de números negativos!")
    else:
        return n*factorial(n-1)
print(factorial(3))

print("\n\n Prueba 1")
values = '1,2,3,4,5'
print(values.split(',')[2])
print(values.split(',')[1])

print("\n\n Prueba 2")
def suma(a,b):
    c = a + b
    return c
print(suma(1,2))

def par_impar(numero):
    if numero%2 == 0:
        return True
    return False
par_impar(9)

def peso_a_euro(pesos):
    euros=pesos/4500
    return euros
peso_a_euro(1000)

def procesar_dato(peso, volumen):
    if peso < 2 and volumen < 0.027:
        return True
    return False
