

#login del sistema
#datos de entrada 
contadorLogin = 3
bandera = False #var de control flag, login
validar =True #var de control flag, menu de registro de productos
error = False #flag menu de registro 
productos = str("")#lista de productos
registro = str("")#registro de productos
opcion = str("")#opciones de menu
contador = int(0) #sumando la cantidad de productos registrado
suma = int(0)#acumula el total de los productos
valor =float(0) #dato de entrada que ingresa el valor del producto

#proceso
while bandera ==False:
    nombre =str(input("Ingrese su usuario:\n"))
    password = str(input("Ingrese su contraseña:\n"))
    contadorLogin -=1

    if(nombre=="Carlos" and password=="MisionTIC_UIS"):
        bandera =True
    elif len(nombre)==0 or len(password)==0:#len indica la longitud de la variable
        print("Usuario y/o password están vacios, intente de nuevo\n")    
        continue
        valor =0
    else:
        print("Credenciales incorrectas")
        print(f"Le quedan {contadorLogin} intentos antes de cerrar el login")
        if contadorLogin ==0:
            bandera= True
            print("Ha bloqueado el sistema de login")
            break
else:
    print("BIENVENIDO AL SISTEMA",nombre)
    while  validar ==True:
        opcion = input("""-----------Menú de registro de productos--------------
         \t 1. Registro de productos
         \t 2. Ver listado de productos
         \t 3. Pagos
         \t 0. Salir del sistema
         \t Ingrese un número válido de las anteriores:\n """)
            #\t tabular \n salto de linea
        if opcion =="1":
            print("registro de productos")
            while registro != "SALIR":
                registro = input("Ingrese el nombre de un producto (Si no desea agregar mas, escriba SALIR)")
                if len(registro) ==0:
                    print("Ingrese un producto por favor no deje un registro vacío")
                else:
                    registro = registro.upper()#convierte la variable registro en mayusculas
                    if registro != "SALIR":
                        contador = contador+1
                        productos += f"{contador} {registro} \n"
                        
        elif opcion == "2":
            print("Listado de productos")
            if len(productos)>0:
                print("La lista de productos registrados son:\n")
                print(productos)
            else: print("NO hay productos en la lista, emplee la opción 1")
        elif opcion == "3":
            print("Pagar")
            for iterar in range(contador):
                valor =float(input(f"Ingrese el valor del producto {iterar+1} {productos} \n"))
                suma = suma+valor
            print("El valor a pagar por la lista de productos es $",suma,"pesos COP")    

        elif opcion =="0":
            print("Termina la ejecución..., adios")
            break
        else:
            print("Ingrese una opción correcta entre 0 y 3")
           