from turtle import *

dim_x = 320
dim_y = 320

pantalla = Screen()

pantalla.setup(dim_x+25,dim_y+25)
pantalla.screensize(dim_x,dim_y)


tortuga = Turtle()
dentro = True


longitud = int(input("Dame la longitud del lado: "))
avanzar = longitud

tortuga.penup()
tortuga.forward(longitud//2)
tortuga.left(90)
tortuga.forward(longitud//2)
tortuga.left(90)
tortuga.pendown()
tortuga.pensize(2)

while dentro:

    for i in ["red","blue","black","green"]:  
        tortuga.pencolor(i)
        tortuga.forward(longitud)
        tortuga.left(90)
    avanzar = avanzar + 10
    longitud = longitud + 10
    
    tortuga.penup()
    tortuga.home()
    tortuga.forward(longitud//2)
    tortuga.left(90)
    tortuga.forward(longitud//2)
    tortuga.left(90)
    tortuga.pendown()
    tortuga.pensize(2)

    if avanzar >= dim_x or avanzar >= dim_y:
        dentro = False
        


tortuga.hideturtle()

pantalla.exitonclick()
