from turtle import *
from random import *

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga = Turtle()

tortuga.shape("turtle") # Tortuga con forma de tortuga.
tortuga.stamp() # Sello de la tortuga en el punto (0,0)

dentro = True # Condicion para finalizar el bucle while.


while dentro:
    distancia = int(input("Dame la distancia entre la tortuga: "))
    angulo = int(input("Dame el angulo de giro: "))
    tortuga.penup()
    tortuga.forward(distancia)
    tortuga.left(angulo)
    tortuga.stamp() # Sello de la tortuga en cada coordenada.

    #Obtenemos las coordenadas de la posicion de la tortuga.
    
    x = tortuga.xcor()
    y = tortuga.ycor()

    #Comprobamos si está dentro de la pantalla.
    
    if x > 200 or x < -200 or y > 100 or y < -100:
        dentro = False

pantalla.exitonclick()
             
    
