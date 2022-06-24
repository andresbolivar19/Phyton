#ejemplo 2
contagio_validado = "No" #variable tipo bandera-flag
paciente ="Lisa"

if (contagio_validado == "No"):
    print("La paciente "+paciente+
    " aún NO se ha realizado su prueba para validar\n"+ 
    "si está contagiada, recomendación:\n\n"+
    "aplicar pruega PCR.")
    contagio_validado = "Pendiente" #cambio de estado de la variable tipo bandera

if (contagio_validado == "Pendiente"):
    print(paciente+ ", verifique su email, fue enviado el resultado de la prueba.")
    contagio_validado = "Si"

if (contagio_validado == "Si"):
    print(paciente+", de acuerdo al resultado de la prueba, haga cuarentena.")
