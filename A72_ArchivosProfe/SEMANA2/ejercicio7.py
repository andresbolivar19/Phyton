#par e impar

#dato de entrada
numero = int(input("Ingrese un numero: "))

#proceso
if not numero%2 ==0:
    print("Impar")
    print(numero**3)
else:
    print("par") 
    print(numero**2)   

#alternativa de solucion
if numero%2 ==0:
    print("---par") 
    print(numero**2) 
else:
    print("**Impar")
    print(numero**3)
      
