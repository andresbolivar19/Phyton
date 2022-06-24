import math as matematica
#from math import sin,pi

def proyectil(angulo,Vo):
    gravedad=9.86
    anguloRadian = (angulo*matematica.pi)/180

    Xmax = int(((Vo**2)*matematica.sin(2*anguloRadian))/gravedad)
    Ymax = int(((Vo**2)*matematica.sin(anguloRadian)**2)/(2*gravedad))

    return Xmax,Ymax
ANGULO = float(input())
VO = float(input())

print(proyectil(ANGULO,VO))

print(proyectil(45,10))
print(proyectil(80,45))

