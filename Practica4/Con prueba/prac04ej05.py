# -*- coding: utf-8 -*-

from modulo_test import test

def expansion_triplete_CAG (cadena):
    nueva = ""
    comparar = "CAG"
    encontrado = 0
    contador = 0
    maximo = 0
    for i in range(len(cadena)):
        contador = contador + 1
        nueva = nueva + cadena[i]
        if contador == 3:
            if nueva == comparar:
                encontrado = encontrado + 1
                contador = 0
                nueva = ""
                if encontrado > maximo:
                    maximo = encontrado
            else:
                encontrado = 0
                contador = 0
                nueva = ""
        
    if maximo == 0:
        return
    else:
        return maximo


# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(expansion_triplete_CAG('GACGAC') == None)
    test(expansion_triplete_CAG('CAGCAG') == 2)
    test(expansion_triplete_CAG('TACGTACGTAT') == None)
    test(expansion_triplete_CAG('CAGCAGTACCTCAGACGT') == 2)
    test(expansion_triplete_CAG('GATCGATCGATGCTAGCTAGCGCATC') == None)
    test(expansion_triplete_CAG('TACTCAGCAGGATGCAGCAGCAGCAGCAG') == 5)
