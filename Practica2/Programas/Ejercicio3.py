##n = int(input("Lados:"))
##lado = int(input("Dimension: "))
#angulo = 360//n
#for i in range(n):
#tortuga.forward(lado)
#tortuga.left(angulo)

from turtle import *

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga = Turtle()

lados = int(input("Dame el numero de lados: "))
longitud = int(input("Dame la longitud del lado: "))


# Dibujamos el rectangulo

if lados == 3:
    for i in range(lados):
        tortuga.forward(longitud)
        tortuga.left(120)


# Dibujamos el cuadrado

if lados == 4:
    for i in range(lados):
        tortuga.forward(longitud)
        tortuga.left(90)


# Dibujamos el pentagono


if lados == 5:
    for i in range(lados):
        tortuga.forward(longitud)
        tortuga.left(72)

# Dibujamos el hexagono
        
if lados == 6:
    for i in range(lados):
        tortuga.forward(longitud)
        tortuga.left(60)

pantalla.exitonclick()
