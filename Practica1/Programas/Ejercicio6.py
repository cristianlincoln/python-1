from turtle import *
from math import *

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(420,220)

tortuga = Turtle()

lado = int(input("Dame el lado: "))
coord_x = int(input("Dame la coordenada x: "))
coord_y = int(input("Dame la coordenada y: "))


diagonal = sqrt(lado**2 + lado**2)

#Crear cuadrado
tortuga.penup()
tortuga.home()
tortuga.forward(lado/2)
tortuga.left(90)
tortuga.pensize(1)
tortuga.pencolor("red")
tortuga.pendown()
tortuga.forward(lado/2)
tortuga.left(90)
tortuga.forward(lado)
tortuga.left(90)
tortuga.forward(lado)
tortuga.left(90)
tortuga.forward(lado)
tortuga.left(90)
tortuga.forward(lado/2)

#Crear circulo
tortuga.penup()
tortuga.home()
tortuga.left(270)
tortuga.forward(diagonal/2)
tortuga.left(90)
tortuga.pendown()
tortuga.pensize(2)
tortuga.pencolor("blue")
tortuga.circle(diagonal/2)

tortuga.penup()

tortuga.goto(coord_x,coord_y)

            
#Pintar las coordenadas

lado_2 = lado/2
radio = diagonal/2

if coord_x < lado_2 and coord_x > -lado_2 and coord_y < lado_2 and coord_y > -lado_2 :
    tortuga.pencolor("red")
    tortuga.dot(5)

elif tortuga.distance(0,0) < radio:
    tortuga.pencolor("blue")
    tortuga.dot(5)

else:
    tortuga.pencolor("green")
    tortuga.dot(5)
    
    

tortuga.hideturtle()

pantalla.exitonclick()
