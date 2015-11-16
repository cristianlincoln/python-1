# -*- coding: utf-8 -*-

from modulo_test import test
from prac04ej04 import contenido_GC
from prac04ej05 import expansion_triplete_CAG

def menu_ADN():
    opcion = 0
    while opcion != 1 and opcion != 2:
        print ("(1) Calcular el GC de una secuencia de ADN")
        print ("(2) Calcular la expansion del triplete 'CGG' de una secuencia")
        opcion = int(input("Elige opción: "))
    return opcion


# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    s = menu_ADN()

    if s == 1:
        cadena = input("Dame una cadena: ")
        print(contenido_GC(cadena))
    elif s == 2:
        cadena = input("Dame una cadena: ")
        print(expansion_triplete_CAG(cadena))
    else:
        print("No es una opcion valida")
            
