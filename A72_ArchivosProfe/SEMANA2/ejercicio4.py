
#datos entrada
nombre1 = str(input("Ingrese el 1er nombre: "))
nombre2 = str(input("Ingrese el 2do nombre: "))

#proceso
#convertir el texto ingresado en mayusculas usando upper()
nombre1Up = nombre1.upper()
nombre2Up = nombre2.upper()
indexNombre1Up = len(nombre1Up)-1 #conocer el ultimo caracter de la variable nombre1Up
indexNombre2Up = len(nombre2Up)-1

if nombre1Up[0] == nombre2Up[0] or\
    nombre1Up[indexNombre1Up] == nombre2Up[indexNombre2Up]:
    print("Coincidencia")
    
else: print("NO hay coincidencia")    
    