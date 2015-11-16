from turtle import *

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga = Turtle()

longitud = int(input("Dame la longitud del lado: "))

tortuga.penup()
tortuga.forward(longitud//2)
tortuga.pendown()
tortuga.left(90)
tortuga.pencolor("red")
tortuga.forward(longitud//2)
tortuga.left(90)
tortuga.pencolor("blue")
tortuga.forward(longitud)
tortuga.left(90)
tortuga.pencolor("black")
tortuga.forward(longitud)
tortuga.left(90)
tortuga.pencolor("pink")
tortuga.forward(longitud)
tortuga.left(90)
tortuga.pencolor("red")
tortuga.forward(longitud//2)

tortuga.hideturtle()

pantalla.exitonclick()
