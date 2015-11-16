def menu_buscaminas():
    opcion = 0
    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
        print ("(1) Destapar casilla")
        print ("(2) Marcar casilla")
        print ("(3) Desmarcar casilla")
        print ("(4) Bombas por detectar")
        print ("(5) Salir")
        opcion = int(input("Elige opción: "))
    return opcion
            



