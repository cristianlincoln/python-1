from turtle import *
from random import *
dim_x = 400
dim_y = 200
pantalla = Screen()
pantalla.setup(dim_x+25,dim_y+25)
pantalla.screensize(dim_x,dim_y)

pirata = Turtle()
dentro = True

while dentro:
    giro = randint(1,360)
    pirata.left(giro)
    pirata.forward(50)


pantalla.exitonclick()
