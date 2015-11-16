# -*- coding: utf-8 -*-

from modulo_test import test
from prac04ej02 import divisores

def son_sociables (lista):
    lista_suma = []
    suma = 0
    sociables = True
    lista_n1 = []

    for num in lista:  
        lista_n1 = divisores(num) # Cargo los divisores
        del lista_n1[-1] # Borra el excluido
            
        for elem in lista_n1:
            suma = suma + elem
        lista_suma.append(suma)
        suma = 0
        
    primero = lista[0] #Guardo el primero de la lista
    ultimo = lista_suma[-1] #Guardo el ultimo
    

    del lista_suma[-1] #Borro el último de la lista
    del lista[0] #Borro el primero de la lista


    #Comparo las listas
    
    for i in range(len(lista)):
        if lista[i] != lista_suma[i]:
            sociables = False
            break

    #Comparo el primero y el último    
    if primero != ultimo:
        sociables = False
        
    return sociables

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(son_sociables([220, 284]) == True)
    test(son_sociables([14288, 15472, 14536, 14264, 12496]) == True)
    test(son_sociables([14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, \
                        589786, 294896, 358336, 418904, 366556, 274924, 275444, \
                        243760, 376736, 381028, 285778, 152990, 122410, 97946, \
                        48976, 45946, 22976, 22744, 19916, 17716]) == True)
    test(son_sociables([28158165, 29902635, 30853845, 29971755]) == True)
