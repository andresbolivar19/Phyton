

from math import log1p


def edad_perro_a_humano(edad=float()):
    resultado = ""
    try:
        if edad>0:
            edadPerro = 16*log1p(edad-1)+31
            edadPerro = round(edadPerro,3)
            resultado +="La edad {} años caninos son edad humana {}"\
            .format(edad,edadPerro)
        else:
            resultado ="La edad ingresada es menor o igual a 0"

    except ValueError as error:
        resultado ="Hay un error "+error
    except (TypeError,ZeroDivisionError):
        resultado ="error "
    except Exception:
        resultado ="Tenemos errores "    
    return resultado

print(edad_perro_a_humano(1))
print(edad_perro_a_humano(2))
print(edad_perro_a_humano(4))
print(edad_perro_a_humano(6))
print(edad_perro_a_humano(0))
print(edad_perro_a_humano("hola"))