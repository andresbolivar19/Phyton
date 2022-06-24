#ejercicio de reconociendo lo aprendido semana 2

#datos de entrada
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

#proceso
notaFinal = (nota1+nota2+nota3+nota4)/4

if notaFinal>=3:
    print("Aprueba la asignatura.",notaFinal)
else:
    print("Reprueba la asignatura.",notaFinal)    
    