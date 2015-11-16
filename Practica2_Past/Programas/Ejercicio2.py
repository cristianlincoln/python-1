from turtle import *
pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga = Turtle()

n = int(input("Dame un numero entero: "))
distancia_max = 0
for i in range(n):
    x = int(input("Dame la coordenada x: "))
    y = int(input("Dame la coordenada y: "))
    tortuga.penup()
    tortuga.goto(x,y)
    tortuga.dot(5)

    if tortuga.distance(0,0) > distancia_max:
        distancia_max = tortuga.distance(0,0)

tortuga.penup()
tortuga.home()
tortuga.forward(distancia_max+5)
tortuga.left(90)
tortuga.pendown()
tortuga.circle(distancia_max)

print("El radio es {0:.2f}" .format(distancia_max))

