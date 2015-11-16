#Importamos modulos que vamos a utilizar en este programa.

from turtle import *
from random import *

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

pirata = Turtle() #Creamos el pirata

pantalla.register_shape("pirata.gif") #Cargamos el gif
pirata.shape("pirata.gif") #Indicamos cual es su sello

tortuga = Turtle() # Creamos la tortuga que dibujara el margen de seguridad

pirata.penup() #Levantamos el pirata para que no deje marca
longitud = 20
dentro = True # Variable para comprobar que el pirata no sale fuera

#Pedimos valores al usuario
pasos = int(input("Dame el numero de paso, 1 paso son 20: "))
radio = int(input("Dame el radio de seguridad: "))


#Dibujamos con la tortuga el circulo de seguridad.

tortuga.penup()
tortuga.forward(radio)
tortuga.left(90)
tortuga.pendown()
tortuga.circle(radio)
tortuga.penup()
tortuga.hideturtle()


# El pirata camina dentro del margen de seguridad
# siempre que se cumpla la condicion de numero de pasos o este dentro.

while pasos > 0 and dentro:

    giro = randint (1,360)
    pirata.left(giro)
    pirata.forward(longitud)
    pasos = pasos - 1

#Comprobación de seguridad.
    
    if pirata.distance(0,0) >= radio:
        dentro = False
        print("Cuidado el pirata está en peligro!")

pantalla.exitonclick()
