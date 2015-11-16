# -*- coding: utf-8 -*-

from modulo_test import test

def crear_lista_digitos(numero):
    lista = []
    while numero > 0:
        numero2 = numero%10
        lista = [numero2] + lista
        numero = numero//10
    return lista

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    numero = int(input("Dame un numero entero: "))
    print(crear_lista_digitos(numero))
        
    
