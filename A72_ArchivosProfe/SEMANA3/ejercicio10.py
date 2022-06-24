
#calculadora
#variable de control bandera
salir = False
opcion = int(0)

#\t => es el tabulador
#\n => salto de linea
while not salir:
    print("""-----------Menú de operaciones matemáticas----------
\t 1. Si desea sumar + ingrese la opción 1
\t 2. Si desea restar - ingrese la opción 2
\t 3. Si desea multiplicar * ingrese la opción 3
\t 4. Si desea dividir / ingrese la opción 4
\t 5. Si desea potencia ** ingrese la opción 5
\t 6. Si desea el residuo o mod de la division '%' ingrese la opción 6
\t 7. Si desea raíz de n ^ ingrese la opción 7
\t 8. Salir del programa digite la opción 8
\t INGRESE UNA OPCIÓN DE LAS ANTERIORES \n""")
    #try except es el manejo de errores 
    num = int(0)
    try:
        num = int(input())
    except Exception as ex:
        print("Error hay una excepción", type(ex))

    opcion = num 
    
    if opcion == 1:
        print("suma")
        dato1 = float(input())
        dato2 = float(input())
        suma = float(dato1+dato2)
        print(f"{dato1} + {dato2} = {suma} \n")#f-strings

    elif opcion ==2:
        print("resta")
        dato1 = float(input())
        dato2 = float(input())
        resta = float(dato1-dato2)
        print(f"{dato1} - {dato2} = {resta} \n")
    elif opcion ==3:
        print("multiplica")
        dato1 = float(input())
        dato2 = float(input())
        multiplicar = float(dato1*dato2)
        print(f"{dato1} * {dato2} = {multiplicar} \n")
    elif opcion == 4:
        print("dividir")
        dato1 = float(input())
        dato2 = float(input())
        try:
            dividir = float(dato1/dato2)
            print(f"{dato1} / {dato2} = {dividir}\n")
        except ZeroDivisionError as error:
            print("Error de división, entre 0 no puede hacer",type(error))
    elif opcion == 5:
        print("potencia")
        dato1 = float(input()) #base
        dato2 = float(input())#exponente
        potencia = float(dato1**dato2)
        print(f"{dato1}^{dato2} = {potencia}\n")
    elif opcion ==6:
        print("mod o residuo de división")
        dato1 = float(input())#dividiendo
        dato2 = float(input())#divisor
        residuo = float(dato1%dato2)
        print(f"{dato1} % {dato2} = {residuo}\n")
    elif opcion == 7:
        print("Raíz de n")
        dato1 = float(input())#radicando el numero dentro del radical
        dato2 = float(input())#indice el num peq del radical
        raiz = float(dato1**(1/dato2))
        #redondeo de decimales con round
        raiz = round(raiz,4)
        print(f"{dato1}^{dato2} = {raiz}\n")
    elif opcion ==8:
        print("Digitó la opción de salir, adios..... =/")
        salir = True#cambio de estado bool a la variable de control bandera a True
    else:
        print("Ingrese un valor entre 1 y 8")


print("Termina la ejecución")
