horas_dia = 24
mes = 31

duracion = int(input("Dame el total de horas: "))

if (duracion < horas_dia or duracion > (horas_dia * mes)):
	print("No es un horario correcto")
else:
        if (duracion >= horas_dia and duracion < 30*horas_dia):
                print("El precio es de 11 €")

        elif (duracion >= (2 * horas_dia) and duracion <= (5 * horas_dia)):
                precio = 11 + ((duracion // horas_dia - 1) * 6)
                print (precio)

        elif (duracion >= (5 * horas_dia) and duracion <= (14*horas_dia)):
                precio = 4 * 6 + 11
                precio = (precio + ((duracion // horas_dia - 5) * 5.5))
                print (precio)
                
        elif (duracion > 14*horas_dia):
                print("El precio es de 110.0 €")
