from turtle import *

dim_x = 600
dim_y = 400

pantalla = Screen()

pantalla.setup(dim_x+25,dim_y+25)
pantalla.screensize(dim_x,dim_y)

tortuga = Turtle()

acabar = True

radio = int(input("Dame el radio del circulo: "))
altura = int(input("Dame la altura: "))

resta = altura

while acabar:
    tortuga.penup()
    tortuga.pendown()
    tortuga.circle(radio)
    tortuga.left(90)
    tortuga.penup()
    tortuga.forward(2)
    tortuga.pendown()
    tortuga.left(-90)
    
    resta = resta - 1

    if resta == 0:
        tortuga.color("black", "white")
        tortuga.begin_fill()
        tortuga.circle(radio)
        tortuga.end_fill()
        tortuga.hideturtle()
        acabar = False
    
