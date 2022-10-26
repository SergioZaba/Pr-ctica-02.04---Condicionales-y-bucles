contraseña = "contraseña"
for i in contraseña:
    verificacion = input("Introduce la contraseña")
    if verificacion == contraseña:
        print("La contraseña es correcta.")
        break
    else:
        print("La contraseña es incorrecta")
