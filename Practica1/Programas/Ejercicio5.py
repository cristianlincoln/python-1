from turtle import *
pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga = Turtle()

coord_x = 0
coord_y = 0

lado = int(input("Dame la longitud del lado: "))

tortuga.penup()
tortuga.goto(coord_x, coord_y)
tortuga.forward(lado/2)
tortuga.left(90)
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
tortuga.penup()
tortuga.goto(coord_x, coord_y)
tortuga.left(180)
tortuga.forward(lado/2)
tortuga.pendown()
tortuga.left(90)
tortuga.circle(lado/2)
tortuga.penup()
tortuga.goto(coord_x,coord_y)
tortuga.pendown()
tortuga.write("({0},{1})" .format(coord_x,coord_y))


pantalla.exitonclick()
