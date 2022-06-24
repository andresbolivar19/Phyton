def calcularCosto(alto, ancho, profundo):
    volumen = alto * ancho * profundo
    costo = volumen * 5
    if (alto > 30):
        costo = costo + 2000
    if (costo > 10000):
        costo = (costo * 0.19) + costo
    return costo

def costoTotal(listaPaquetes, descuento):
    total = 0
    for iterador in listaPaquetes:
        alto = iterador['ALTO']
        ancho = iterador['ANCHO']
        profundo = iterador['PROFUNDO']
        
        total += calcularCosto(alto, ancho, profundo)
    return total*(1-descuento/100)