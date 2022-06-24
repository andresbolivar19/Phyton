def calcularCosto(alto, ancho, profundo):
    volumen = alto * ancho * profundo
    costo = volumen * 5
    if (alto > 30):
        costo = costo + 2000
    if (costo > 10000):
        costo = costo * 0.19 + costo
    return(costo)

def costoTotal(numeroPaquetes, descuento):
    costoTotal = 0
    for n in range(numeroPaquetes):
        alto = float(input())
        ancho = float(input())
        profundo = float(input())
        costoTotal += calcularCosto (alto, ancho, profundo)
    costoTotal -= (costoTotal * descuento / 100)
    return costoTotal
print(calcularCosto(35,10,5))
print(costoTotal(2, 50))
print(costoTotal(2, 0))
