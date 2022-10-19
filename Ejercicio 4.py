edad = int(input("introduzca su edad"))
ingresos = float(input("introduzca sus ingresos mensuales"))

if edad > 16 and ingresos >= 1000:
    print("usted debe tributar")
else:
    print("usted no debe tributar")