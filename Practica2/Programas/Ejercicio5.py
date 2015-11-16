from turtle import *

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga = Turtle()
suma_puntos = 0
r = float(input("Dame el valor del radio: "))
n = int(input("Dame el numero de puntos: "))

#Dibujamos el circulo

tortuga.penup()
tortuga.forward(r)
tortuga.left(90)
tortuga.pendown()
tortuga.circle(r)
tortuga.penup()


for i in range(n):
    coord_x = int(input("Dame la coordnada x: "))
    coord_y = int(input("Dame la coordenada y: "))
    tortuga.goto(coord_x,coord_y)
    tortuga.dot(5)

    if tortuga.distance(0,0) < r:
        suma_puntos = suma_puntos + 1

print("El numero de puntos total dentro del circulo es {0}." .format(suma_puntos))
    
pantalla.exitonclick()
