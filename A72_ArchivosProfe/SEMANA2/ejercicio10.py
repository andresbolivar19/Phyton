
#dato de entrada
angulo = int(input("Ingrese un valor: "))

grados = 360
Angulo = angulo/grados
Angulo1 = abs(Angulo)-abs(int(Angulo))
#abs() valor absoluto de un numero, abs(-56) rta=56 
# en math es=|56|
print(Angulo,Angulo1) 

if angulo>=0:
    if Angulo1<=0.25:
        print("1er cuadrante del plano", angulo)
    elif Angulo1<=0.5:
        print("2do cuadrante del plano", angulo)
    elif Angulo1 <=0.75: 
        print("3er cuadrante del plano", angulo)
    else:
        print("4to cuadrante del plano", angulo)   

else:    
    print("Valor negativo")