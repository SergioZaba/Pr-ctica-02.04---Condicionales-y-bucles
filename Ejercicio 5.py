nombre = input("introduzca su nombre \n")
sexo = input("introduzca H si es hombre o M si es mujer \n")
nombre = nombre[0]
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in letras:
    if sexo.upper() == "M" and nombre.lower() < letras[12]:
        print("Usted es de Gryffindor")
        break
    if sexo.upper() == "H" and nombre.lower() > letras [13]:
        print("Usted es de Gryffindor")
        break
    else:
        print("Usted es de Slytherin")
        break