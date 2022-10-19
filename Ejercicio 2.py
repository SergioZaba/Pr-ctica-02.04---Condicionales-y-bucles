numerador = float(input("introdizca el numerador"))
denominador = input("introdizca el denominador")

if denominador == "0":
    print("error, el denominador no puede ser 0")
else:
    denominador = float(denominador)
    division = numerador / denominador
    print("el resultado es", division)