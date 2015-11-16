# -*- coding: utf-8 -*-

from modulo_test import test

def es_cuadrado_latino (matriz):
    filcol = len(matriz)
    col = len(matriz)
    fil = len(matriz[0])
    es_latino = True
    for fil in range(filcol):
        for col in range(filcol):
            if matriz[fil][col] in matriz[fil][col+1:]:
                es_latino = False
                break
            else:
                for restofil in range(fil+1,filcol):
                    if matriz[fil][col] == matriz[restofil][col]:
                        es_latino = False
                        break
    return es_latino

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!
    matriz2=[[1,2,3], \
             [2,3,1], \
             [3,1,2]]
    matriz3=[[1,2,3,4], \
             [2,1,4,3], \
             [3,4,1,2], \
             [4,3,2,1]]
    matriz4=[[1,2,3,4], \
             [3,4,1,2], \
             [4,3,2,1], \
             [2,1,4,3]]
    matriz5=[[1,2,3], \
             [0,3,1], \
             [3,1,2]]
    matriz6=[[1,2,3], \
             [2,3,4], \
             [3,1,2]]
    matriz7=[[1,2,3], \
             [2,3,1], \
             [1,2,3]]
    matriz8=[[1,2,3,4], \
             [2,1,4,3], \
             [3,4,1,2], \
             [1,3,2,4]]

    test(es_cuadrado_latino(matriz2) == True)
    test(es_cuadrado_latino(matriz3) == True)
    test(es_cuadrado_latino(matriz4) == True)
    test(es_cuadrado_latino(matriz5) == False)
    test(es_cuadrado_latino(matriz6) == False)
    test(es_cuadrado_latino(matriz7) == False)
    test(es_cuadrado_latino(matriz8) == False)
