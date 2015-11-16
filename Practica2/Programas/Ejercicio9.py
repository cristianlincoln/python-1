from turtle import *
from random import *

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga = Turtle()

continuar = True

trazos = int(input("Dame el numero total de trazos: "))

while continuar:
    
    for i in range(trazos):
        
        grosor = randint(1,20) #Grosor del trazo

        #Valores para el RGB
        
        valor_rojo = random()
        valor_verde = random()
        valor_azul = random()

        tortuga.color(valor_rojo, valor_verde, valor_azul) # Cambiar el color de la tortuga

        #Coordenadas dentro de la pantalla
        
        coord_x = randint(-200,200)
        coord_y = randint(-100,100)

        #Grosor del lapiz
        tortuga.pensize(grosor)
        
        #Mover tortuga a las coordenadas indicadas.
        tortuga.goto(coord_x, coord_y)

    correcto = True
    
    while correcto:   
        otra = input("Desea realizar otra pasada (s)/(n): ")

        if otra == "n":
            correcto = False
            continuar = False
        elif otra == "s":
            correcto = False
        else:
            print("No es una respuesta valida")

pantalla.exitonclick()

    

                 
        

