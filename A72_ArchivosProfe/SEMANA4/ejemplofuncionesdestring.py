
#funciones de cadenas de caracteres

caracteres = 'asombroso'
valor = 'as'
print(caracteres.count(valor))#cuenta cuantas veces existe un valor es decir una letra o texto en una frase
print(caracteres.capitalize())#convierte la 1era letra en mayuscula

caracteres = "Hola a todos, este su nuevo bienvenidos a este curso"
valor = "este"
print(caracteres.find(valor)) #busca en que posición esta una palabra o letra en una frase

caracteres = "1+2-3-4-5 6"
print(caracteres.split()) #separa los caracteres de acuerdo a lo que se ponga en el split si no hay nada asume un espacio

letras = "abcdefg hola mundo"
delimitador = "**"
print( delimitador.join(letras))#delimita el texto con lo que queramos un salto de linea, comas, punto y coma, etc
print("join de una lista")
letras = ["Hola", "como", "estas"] #es una lista
print(letras)
delimitador = "\n"
print( delimitador.join(letras)) # separa esa lista letras en un texto  


#replace
frase ="Bienvenidos a clase estudiantes python A72 no olvide hacer la asistencia en moodle"
print("Texto sin modificar \n", frase)
frase = frase.replace("estudiantes","tripulantes")
print("texto modificado con replace: \n",frase)

#casefold
palabra = "HOLA"
palabra1 = "hola"


print(palabra.casefold()==palabra1.casefold())


###########

#importar modulos predefinidos en python

#1. from modulo import las funciones o constantes de ese modulo, todo separado por comas
from math import e,sqrt
print("resultados de la libreria math usando from math import e, sqrt")
print(e)
print(sqrt(12))

#2.importar el modulo y colocando un alias usando 'as'
import os as sistemaOperativo
#print(sistemaOperativo.system("clear")) #windows  system("cls")
print("terminal ha quedado practicamente sin informacion")

#3.si necesita usar varios modulos separados por comas:
import datetime, json, sys
print("datetime modulo fecha:")
print(datetime.date.today())
fecha = datetime.datetime.now()
print(fecha)