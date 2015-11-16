from turtle import *

pantalla = Screen()
pantalla.setup(525,325)
pantalla.screensize(500,300)

tortuga = Turtle()

lados = int(input("Dame el numero de lados: "))
longitud = int(input("Dame la longitud del lado: "))
radio = int(input("Dame el radio de los circulos: "))


# Dibujamos el rectangulo
        
contador = 3
if lados == 3:
 
    while contador > 0:
        tortuga.left(240)
        for i in range(lados):
            tortuga.circle(radio)
            tortuga.forward(longitud / 3)
        contador = contador - 1 


# Dibujamos el cuadrado

contador = 4
if lados == 4:


    while contador > 0:
        tortuga.left(270)
        for i in range(lados):
            tortuga.circle(radio)
            tortuga.forward(longitud / 4)
        contador = contador - 1 


# Dibujamos el pentagono

contador = 5
if lados == 5:
 
    while contador > 0:
        tortuga.left(72)
        for i in range(lados):
            tortuga.circle(radio)
            tortuga.forward(longitud / 5)
        contador = contador - 1 

# Dibujamos el hexagono

contador = 6
if lados == 6:
 
    while contador > 0:
        tortuga.left(60)
        for i in range(lados):
            tortuga.circle(radio)
            tortuga.forward(longitud / 6)
        contador = contador - 1


pantalla.exitonclick()
