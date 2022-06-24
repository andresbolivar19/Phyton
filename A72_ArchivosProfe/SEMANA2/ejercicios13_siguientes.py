#EJERCICIO 13
SALARIO = float(input('Ingrese el valor del total del contrato: '))
RIESGO = int(input('Indique el nivel de riesgo (escriba 1,2,3,4 o 5 ) '))

if 1e6<=SALARIO<2.5e6:
    SALARIO =SALARIO 
else:
    SALARIO*=0.4  #si el salario supera 2500000 se calcula por el 40% el ibc
IBC = round(SALARIO,2) #redondear 2     
if 1<=RIESGO<=5:
    if RIESGO == 1:
        Riesgo = round(0.00522*IBC,2) #nivel 1 0.522%
    elif RIESGO ==2:
        Riesgo = round(0.01044*IBC,2) #nivel 2 1.044%
    elif RIESGO ==3:
        Riesgo = round(0.02436*IBC,2) #nivel 3 2.436%
    elif RIESGO ==4:
        Riesgo = round(0.04350*IBC,2) #nivel 4 4.350%
    elif RIESGO ==5:
        Riesgo = round(0.06960*IBC,2) #nivel 1 6.96%
else:
    print('Nivel de riesgo no válido')
    
SALUD = round(IBC*0.125,2)
PENSION = round(IBC*0.16,2)
print(f'Salud ${SALUD}\nPensión ${PENSION} \nRiesgo ${Riesgo}')    
PILA = "{:.2f}".format(SALUD+PENSION+Riesgo)
print(PILA)    

print(f'\n\nPago de la seguridad social es:\n\
PILA: {round(float(PILA),-2)}\n\
Salud: $ {round(SALUD, -2)} pesos,\nPensiòn: $ {round(PENSION, -2)} pesos,\nARL: $ {round(Riesgo,-2)} pesos')#Si el segundo argumento es negativo, se redondea a decenas, centenas, etc.
#EJERCICIO 14

#EJERCICIO 15
cantidad_computadoras = int(input("¿Cuántas PC's compró? "))
precio_computadora = 985000
compra_sin_dcto = precio_computadora*cantidad_computadoras
if cantidad_computadoras <5:
  compra_con_dcto = compra_sin_dcto*0.9
  print("El valor a pagar con dcto es %.2f" %(compra_con_dcto))

elif cantidad_computadoras <10: # 5<= cantidad_computadoras<10
  compra_con_dcto = compra_sin_dcto*0.8
  print("El valor a pagar con el 80% dcto es {:.2f}" .format(compra_con_dcto))

elif cantidad_computadoras>= 10:
  compra_con_dcto = compra_sin_dcto*0.6
  print("El valor a pagar con  el 60% dcto es {:.2f}" .format(compra_con_dcto))

else:  
  print("La cantidad es negativa")
#EJERCICIO 16

#EJERCICIO 17
numero_hectareas = int(input("Ingrese el valor de hectareas del bosque: "))
metros_cuadrados = numero_hectareas *10000 #conversor de hect a metros

if metros_cuadrados > 1000000:
  metros_pinos = metros_cuadrados *0.7
  metros_oyamel = metros_cuadrados *0.2
  metros_cedro = metros_cuadrados *0.1

  print("Metros^2 pinos " , int(metros_pinos),
    "\nMetros^2 oyamel ", int(metros_oyamel),
    "\nMetros^2 cedro " , int(metros_cedro))
else:    
  metros_pinos = metros_cuadrados *0.5
  metros_oyamel = metros_cuadrados *0.3
  metros_cedro = metros_cuadrados *0.2

  print("Metros^2 Pinos " , int(metros_pinos),
    "\nMetros^2 Oyamel ", int(metros_oyamel),
    "\nMetros^2 Cedro " , int(metros_cedro))

num_pinos = int((metros_pinos/10)*8)
num_oyamel = int((metros_oyamel/15)*15)
num_cedro = int((metros_cedro/18)*10)

print("# Pinos " , num_pinos,
    "\n# Oyamel ", num_oyamel,
    "\n# Cedro " ,num_cedro)

#EJERCICIO 18
# mayor a $ 1.000.000 el interés a pagar será del 5% del
# monto solicitado.
#  Si el monto está entre $ 750.000 y $ 1.000.000 el interés a pagar será
# del 3.85% del monto solicitado.
#
# Si el monto está entre $ 500.000 y $ 750.000 el interés a
#  pagar será del 2.5% del monto solicitado.
#
# Y si el monto es inferior a $ 500.000 el interés a
# pagar será del 1.75% del monto solicitado.

credito = int(input("Introduzca el monto del crédito \n"))
monto = int(0)
interes1 = 0.05 #5/100
interes2 = 0.0385 #3.85/100
interes3 = 0.025 #2.5/100
interes4 = 0.0175 #1.75/100
if credito > 1000000:
    monto = int(credito*interes1)
elif credito > 750000 and credito <=1000000:
    monto = int(credito*interes2)
elif credito > 500000 and credito <= 750000:
    monto = int(credito*interes3)
else:
    monto = int(credito*interes4)
print(monto)

#EJERCICIO 19

#TRES datos de entrada A,B y C
#discriminante b^2-4*a*c

A = int(input("Introduzca el coeficiente A \n"))
B = int(input("Introduzca el coeficiente B \n"))
C = int(input("Introduzca el coeficiente C \n"))

#CONDICIONALES
#Si b^2-4ac < 0 Entonces, la ecuación no tiene solucion real
#Si b^2-4ac > 0 Entonces, la ecuación tiene dos soluciones distintas
#Si b^2-4ac = 0 Entonces, la ecuación tiene una única solución
discriminante = (B**2)-(4*A*C)
rta = str("")
x1 = float(0.0)
x2 = float(0.0) 
if discriminante<0:
    rta ="no tiene solucion real"
    x1 = (-B+(discriminante**0.5))/(2*A)
    x2 =(-B-(discriminante**0.5))/(2*A)
    
elif discriminante > 0:
    rta ="tiene dos soluciones reales"
   
    x1 = (-B+(discriminante**0.5))/(2*A)
    x2 =(-B-(discriminante**0.5))/(2*A)
else:
    rta ="tiene una unica solucion"   
    x1 = (-B+(discriminante**0.5))/(2*A)
    x2 =(-B-(discriminante**0.5))/(2*A)   
     
print(rta,x1,x2)