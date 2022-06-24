

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
delimitador = " "
print( delimitador.join(letras)) # separa esa lista letras en un texto 