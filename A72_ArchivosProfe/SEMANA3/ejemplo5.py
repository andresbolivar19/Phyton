#ciclo for (para)

#for i (iterador) in elemento Iterable(lista, cadena, range)

#for con range(inicio, fin, + o -)
manzanas = 0# int(input("Ingrese la cantidad de manzanas a agregar en la cesta: "))
for i in range(1,manzanas+1,1):
    
    print("ahora hay",i,"manzanas")
    
texto = "hola mundo"
longitudTexto = len(texto)
print("longitud de texto",longitudTexto)
buscar = str("a")
contador =0

for i in texto:
    print(i)

#funcion range(I, F, P) crea una lista de acuerdo a esos parametros
#I = inicio de la lista, por defecto 0
#F = Final de la lista, la cual no va a llegar al valor que se asigne alli, F-1, es decir F=10, va iterar hasta 9
#P= pasos, incremento/decremento, por defecto +1

#1. range (I,F,P)
for iterador in range(10,0,-2): 
    #10 es inicio de la iteracion, 0 fin de la iteracion sin tenerlo en cuenta 2, -2 los pasos
    print(iterador)

#2. range(I,F)
for sumador in range(1,10):
     #1 es inicio, 10 final de la iteracion sin tenerlo en cuenta 10-1=9, pasos por defecto es +1
     print(sumador)

#3.  range(F)
for i in range(longitudTexto): 
    #longitudTexto es final de la iteracion sin tenerlo en cuenta, para el eje la var = 10-1=9
    
    caracter = texto[i]
    print(f"En el indice {i} esta la letra {texto[i]}")

    #buscar una letra en una cadena de texto
    if caracter== buscar:
        contador +=1
    #else: print(f"La letra a buscar \'{buscar}\' NO esta en la frase \'{texto}\'")

print(f"La letra a buscar \'{buscar}\' esta {contador} veces en la frase \'{texto}\'")