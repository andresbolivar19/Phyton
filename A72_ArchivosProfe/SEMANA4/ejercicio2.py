#empleando *
def peso_a_euro(*pesos): 
    listado = []#lista vacia 
    for i in pesos:
        euros = float(i/4500)#conversion de peso a euro
        euros = round(euros,2)
        rta = "$ {} pesos = {} euros ".format(i,euros)
        listado.append(rta)
    return listado

print(peso_a_euro(4500,9000,25000,45000,789000,980540))