#funciones sin argumento sin return
def miFuncion():
    valor=str(input("Ingrese su nombre: "))
    print("Su nombre es ",valor)
    #return valor
print(miFuncion())

name = str(input("su nombre: "))
lastName = str(input("su apellido: "))
age = int(input("su edad: "))
#funcion con 3 argumentos, un valor por defecto de uno de los argumentos y return
def funcion(nombre,apellido=str("sin datos"), edad=int()):
    informacion = "Hola {} {} su edad es {} años"
    informacion = informacion.format(nombre,apellido,edad)

    return informacion
    
print(funcion("pep","zidane",33))
#siguiente print omite el argumento apellido el cual tiene un valor por defecto
print(funcion(nombre="Carlos", edad=28))
print(funcion(name,lastName,age))




