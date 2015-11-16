##
##pedir = True
##while pedir:
##    numero = int(input("Dame un numero del 1 al 100: "))
##    if numero < 100 and numero > 0:
##        pedir = False

from random import *

print("Piensa un número del 1 al 100,¡voy a intentar advinarlo!")
print("Pulsa intro cuando estés listo...")
input()
aleatorio = randint(1,100)
acierto = True
while acierto:
    respuesta = input("¿Es el {0} el número secreto? (s/n) " .format(aleatorio))
    if respuesta == "n":
        mayor_menor = input("¿Es el número secreto mayor o menor que {0}?. ".format(aleatorio))
        if mayor_menor == "mayor":
            aleatorio = randint(aleatorio+1, 100)
        elif mayor_menor == "menor":
            aleatorio = randint(0,aleatorio-1)
    elif respuesta == "s":
        print("Estoy de suerte, ¡He acertado!")
        acierto = False
    else:
        print("Lo siento no te he entendido")
    
    

