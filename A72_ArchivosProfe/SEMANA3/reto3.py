costoTotal = 0
numeroPaquetes = int(input())
for i in range(numeroPaquetes):
  alto = float(input())
  ancho = float(input())
  profundo = float(input())
  volumen = alto*ancho*profundo
  costo = volumen * 5
  if alto > 30:
    costo += 2000
  if costo > 10000:
    costo *= 1.19
  costoTotal += costo
  print (volumen)
  print (costo)
print (costoTotal)
