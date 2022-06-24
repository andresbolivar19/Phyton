#ejercicio 2
#datos de entrada
numero1 = int(input("Escriba el 1er num: "))
numero2 = int(input("Escriba el 2do num: "))
numero3 = int(input("Escriba el 3er num: "))
''' ''' #alt+3+9='

#proceso
if numero1 == numero2 and numero1==numero3 and numero3==numero2:
    print("Los 3 numeros son iguales.")
    menor = numero1
    medio = numero2
    mayor = numero3
elif ( (numero1 >= numero2) and (numero1 >= numero3) ):
    mayor = numero1
    print("1er if se cumple")
    #if anidado
    if numero2<= numero3:
        medio = numero2
        menor = numero3
        print("if anidado del 1er if")
    else:
        medio = numero3
        menor = numero2
        print("else del if anidado 1")
elif numero2 >=numero1 and numero2>=numero3:
    mayor = numero2   
    print("Elif")
    #if anidado        
    if numero1<= numero3:
        medio = numero1
        menor = numero3
        print("if del elif")
    else:    
        medio = numero3
        menor = numero1
        print("else del elif")
else:
    mayor = numero3
    print("Else final")
    if numero1<=numero2:
        medio = numero1
        menor = numero2
        print("if anidado del Else final")

    else:
        print("else anidado del Else final")
        
        medio = numero2
        menor = numero1

print(menor,medio,mayor)
