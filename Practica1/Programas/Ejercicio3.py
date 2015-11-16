#Importamos todo del modulo turtle y la raiz cuadrada del modulo math

from turtle import *
from math import sqrt

#Inicializamos la pantalla

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

#Inicializamos la tortuga

tortuga = Turtle()

#Inicializamos las coordenadas
coord_x = 0
coord_y = 0

#Pedimos al usuario el tamaño del lado

lado = int(input("Dame el tamaño del lado: "))

#Calculamos la hipotenusa
hipo = sqrt(lado**2 + lado**2)/2

tortuga.penup()
tortuga.goto(coord_x,coord_y)
tortuga.pendown()
tortuga.goto(lado,coord_y)
tortuga.goto(lado,lado)
tortuga.goto(coord_x,lado)
tortuga.goto(coord_x,coord_y)

tortuga.goto(lado,lado)
tortuga.penup()
tortuga.goto(coord_x,lado)
tortuga.pendown()
tortuga.goto(lado,coord_y)
tortuga.penup()
tortuga.goto(lado,lado)

#Dibujamos el techo de la casa

tortuga.pendown()
tortuga.left(135)
tortuga.forward(hipo)
tortuga.left(90)
tortuga.forward(hipo)
tortuga.penup()
tortuga.goto(coord_x,coord_y)
tortuga.pendown()

#Escribimos las coordenadas
tortuga.write("({0},{1})".format(coord_x,coord_y))

#Escondemos la tortuga
tortuga.hideturtle()

#Pulsamos para salir
pantalla.exitonclick()
