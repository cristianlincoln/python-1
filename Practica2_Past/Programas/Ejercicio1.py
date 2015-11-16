from turtle import *

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga = Turtle()

n = int(input("Dame un numero entero: "))
media = 0
for i in range(n):
    x = int(input("Dame la coordenada x: "))
    y = int(input("Dame la coordenada y: "))
    tortuga.penup()
    tortuga.goto(x,y)
    tortuga.dot(5)
    media = tortuga.distance(0,0) + media / n

print("La distancia media es: {0:.2f}." .format(media))

pantalla.exitonclick()






