#lista de compras 
#variables acumuladores

listaCompras = ""
print("Iniciando la lista de compras..")
listaCompras = listaCompras+"5 manzanas"
print("---Lista de compras---")

listaCompras = listaCompras+"\n3 Lb Cilantro" #\n es salto de línea
print("---Lista de compras---")

listaCompras = listaCompras + "\n3 Lb Perejil"
print("---Lista de compras---")
print(listaCompras)


precioManzana = 1200
cantManzanas = 5 #puede usar input
precioCilantro = 200
cantCilantroLb = 3
precioPerejil = 300
cantPerejilLb = 3
#acumulador 
subTotal =0

print("Calculando total del mercado")

totalManzana = precioManzana*cantManzanas
subTotal = subTotal +totalManzana
print(subTotal)

totalCilantro = precioCilantro*cantCilantroLb
subTotal = subTotal+totalCilantro
print(subTotal)

totalPerejil = precioPerejil*cantPerejilLb
subTotal = subTotal+totalPerejil
print("El total a pagar es:",subTotal)

