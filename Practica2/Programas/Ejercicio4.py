from turtle import *

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga = Turtle()

pelda = int(input("Dame el numero de peldaños: "))
longitud = int(input("Dame la longitud del peldaño: "))


tortuga.forward(longitud * pelda)
tortuga.left(90)

for i in range (pelda):
    tortuga.forward(longitud)
    tortuga.left(90)
    tortuga.forward(longitud)
    tortuga.right(90)
    

tortuga.left(180)
tortuga.forward(longitud * pelda)

pantalla.exitonclick()
