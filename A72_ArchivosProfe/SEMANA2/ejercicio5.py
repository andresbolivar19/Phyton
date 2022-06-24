
#dato de entrada

letra = str(input("Ingrese una letra: "))

#proceso

if len(letra) >=1 or letra in "0123456789":
    print("Ingresó un numero")  

elif len(letra) ==1:    
    if letra.lower() in "aeiou":
        print("Es una vocal",letra.lower())
      
    else:
        print("Es una consonante",letra.lower())    

else: print("No se puede procesar")    
