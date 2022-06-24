def procesar_dato(peso=float ,volumen=float):
    if peso <2 and volumen<0.027:
        resultado = True
    else: resultado = False

    return resultado

peso = float(input("Ingrese el peso del paq: "))
volumen = float(input("Ingrese el vol del paq: "))

print(procesar_dato(peso,volumen))
#2
print(procesar_dato(5,0.015))
#3
print(procesar_dato(peso=1,volumen=0.014))

###
def PROCESAR_DATO(*args):
   PESO = args[0]
   VOL = args[1]

   if PESO<2 and VOL<0.027:
       resultado = True
   else: resultado = False

   return resultado

print("2da alternativa usando * ")   
print(PROCESAR_DATO(1.98,0.0269))