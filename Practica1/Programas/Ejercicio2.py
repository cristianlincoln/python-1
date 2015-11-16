# Visualizar un cuadrado con su vértice inferior izquierdo en el origen

from turtle import *

#Inicializamos la pantalla

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

#Asignamos las variables x e y, y pedimos al usuario valores del lado
x = 0
y = 0
lado = int(input("Dame el tamaño del lado: "))

#Inicializamos la tortuga
tortuga = Turtle()
tortuga.penup()
tortuga.home()
tortuga.pendown()

#Dibujamos lado con sus coordenadas.
coord_x = tortuga.xcor()
coord_y = tortuga.ycor()
tortuga.write(("({0},{1})").format(coord_x,coord_y))
tortuga.goto(lado,y)

#Dibujamos lado con sus coordenadas.
coord_x = tortuga.xcor()
coord_y = tortuga.ycor()
tortuga.write(("({0},{1})").format(coord_x,coord_y))
tortuga.goto(lado,lado)

#Dibujamos lado con sus coordenadas.
coord_x = tortuga.xcor()
coord_y = tortuga.ycor()
tortuga.write(("({0},{1})").format(coord_x,coord_y))
tortuga.goto(x,lado)

#Dibujamos lado con sus coordenadas.
coord_x = tortuga.xcor()
coord_y = tortuga.ycor()
tortuga.write(("({0},{1})").format(coord_x,coord_y))

tortuga.home()
tortuga.hideturtle()

pantalla.exitonclick()




