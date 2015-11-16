# -*- coding: utf-8 -*-

from modulo_test import test
from prac04ej02 import divisores

def son_amigos (n1,n2):
    amigos = False
    lista_n1 = []
    lista_n2 = []
    suma_n1 = 0
    suma_n2 = 0
    lista_n1 = divisores(n1)
    lista_n2 = divisores(n2)

    del lista_n1[-1]
    del lista_n2[-1]

    for elem in lista_n1:
        suma_n1 = suma_n1 + elem
        
    for elem in lista_n2:
        suma_n2 = suma_n2 + elem
        
    if suma_n1 == n2 and suma_n2 == n1:
        amigos = True
        
    return amigos

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(son_amigos(30, 42) == False)
    test(son_amigos(42, 30) == False)
    test(son_amigos(220, 284) == True)
    test(son_amigos(284, 220) == True)
    test(son_amigos(2620, 2924) == True)
    test(son_amigos(6368, 6232) == True)
