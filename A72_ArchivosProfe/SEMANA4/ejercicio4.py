from math import sqrt as raiz

def area_triangulo(a,b,c):
    semiPerimetro = (a+b+c)/2
    if a+b >= c:
        Area = raiz(semiPerimetro*(semiPerimetro-a)*(semiPerimetro-b)*
        (semiPerimetro-c))
        Area = round(Area,4)
    else:
        Area ="No se puede crear el triangulo con esos datos"    
    
    return Area


print(area_triangulo(1,1,1))
print(area_triangulo(4,6,5))
print(area_triangulo(2,1,4))
