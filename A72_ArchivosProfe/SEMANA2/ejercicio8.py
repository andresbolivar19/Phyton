#datos de entrada

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
nota5 = float(input())

if 1<=nota1 <= 5 and 1<=nota2 <=5\
    and 1<=nota3<=5 and 1<=nota4<=5\
    and 1<=nota5<=5:

    operacion1 = nota1*0.15 #15/100
    operacion2 = nota2*0.3
    operacion3 = nota3*0.25
    operacion4 = nota4*0.1
    operacion5= nota5*0.2

    notaFinal =operacion1+operacion2+operacion3+operacion4+operacion5
    #redondeo de decimales con round
    notaFinal = round(notaFinal,2)
    if  notaFinal>=3.0:
        print("Aprueba la asignatura {}".format(notaFinal))
    else:
        print("No aprueba la asignatura ",notaFinal)

else: print("Alguna de las notas está fuera del rango")    