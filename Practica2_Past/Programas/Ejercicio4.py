from turtle import *
pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)


tortuga = Turtle()
tortuga.left(90)
tortuga.shape("turtle") # Tortuga con forma de tortuga.
tortuga.stamp() # Sello de la tortuga en el punto (0,0)

for i in range(12):
    tortuga.penup()
    tortuga.forward(50)
    tortuga.stamp()
    tortuga.backward(50)
    tortuga.left(30)
    
pantalla.exitonclick()
