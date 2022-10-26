numero = int(input("Escriba un numero entero \n"))

for i in range(1, numero+1, 2):
    for m in range(i,0,-2):
        print(m,end=" ")
    print("")
