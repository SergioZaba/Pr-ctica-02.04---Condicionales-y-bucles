frase = input("Introduce una frase")
letra = input("Introduce una letra")
cuenta = 0
for i in frase:
    if i == letra.lower():
        cuenta = cuenta+1
print("El numero de veces que aparece su letra en la frase es:",cuenta)