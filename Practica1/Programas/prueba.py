duracion = int(input("Dame el total de horas: "))

dias = duracion // 24

if duracion < 24 or duracion > (24*31):
    print("No es un horario correcto")
else:
    if (dias == 1):
        print("El precio es de 11 €")
    elif (dias >= 2 and dias < 5):
        precio = 11 + ((dias-1) * 6)
        print(precio)
    elif (dias >= 5 and dias <=14):
        precio = 4 * 6 + 11
        precio = (precio + (dias - 5*5.5))
        print(precio)
    elif (duracion > dias):
        print("El precio es de 1100€")

