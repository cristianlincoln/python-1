# -*- coding: utf-8 -*-

from modulo_test import test

##def contenido_GC (cadena):
##    porcentaje = 100
##    contador = 0
##    resultado = 0
##    for caracter in cadena:
##        if caracter == "G" or caracter == "C":
##            contador = contador + 1
##    resultado = round(contador / len(cadena) * porcentaje,2)  
##    return resultado

def contenido_GC(cadena):
    contador = 0
    distinto = 0
    resultado = 0
    for caracter in cadena:
        if caracter == "G" or caracter == "C":
            contador = contador + 1
    resultado = round(100 / len(cadena) * (len(cadena) - contador),2)
    return resultado

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(contenido_GC('GCGC') == 100.0)
    test(contenido_GC('CGCG') == 100.0)
    test(contenido_GC('GACGAC') == 66.67)
    test(contenido_GC('TACGTACGTAT') == 36.36)
    test(contenido_GC('CAGTACTACCTCAGACGT') == 50.0)
    test(contenido_GC('GATCGATCGATGCTAGCTAGCGCATC') == 53.85)
