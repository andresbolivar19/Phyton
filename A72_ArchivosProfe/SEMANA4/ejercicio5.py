def sumar(x,y):
    if isinstance(x,int) and isinstance(y,int):
        return x+y
    else: raise TypeError("Los argumentos deben ser enteros")

try:
    print(sumar(15,45))
    print(sumar(155255,8975))
    print(sumar(15,45.25))
    print(sumar("15","45"))
except TypeError as error:
    print(error)    