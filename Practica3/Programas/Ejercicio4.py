from random import *

aleatorio = ""

while len(aleatorio) < 4:
    n1 = str(randint(1,9))
    if n1 not in aleatorio:
        aleatorio = aleatorio + n1
print(aleatorio)

lista = []
acierto = False
vacas = 0
toros = 0

while not acierto:
    lista = []
    toros = 0
    vacas = 0
    cadena = input("Se ha generado un codigo aleatorio de  4 digitos: ")
    
##Modificar, comprobación cadena = aleatorio
    
    for i in range(len(cadena)):
        if cadena[i] == aleatorio[i]:
            toros = toros + 1
            
            
        elif cadena[i] in aleatorio:
            vacas = vacas + 1

         

    if toros == 4:
        acierto = True
        print("Has acertado!")
    else:
        print("HAS FALLADO: {0} toros y {1} vacas" .format(toros, vacas))      
        
    
