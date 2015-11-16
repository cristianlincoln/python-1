# -*- coding: utf-8 -*-

def leer_matriz_enteros():
    matriz = []
    filas = int(input("Dame el número de filas: "))
    columnas = int(input("Dame el número de columnas: "))
    for fil in range(filas):
        matriz.append([0]*columnas)
    for fil in range(filas):
        for col in range(columnas):
            matriz[fil][col] = int(input("Dame valores para la matriz: "))
    return matriz

def mostrar_matriz_enteros(matriz):
    for fil in range(len(matriz)):
        for col in range(len(matriz)):
            print(matriz[fil][col], end=" ")
        print()

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    matriz = leer_matriz_enteros()
    mostrar_matriz_enteros(matriz)
    print(matriz)
    respuesta = input("Quieres crear otra matriz?(s/n) ")
    while respuesta == "s":
        matriz = leer_matriz_enteros()
        mostrar_matriz_enteros(matriz)
        respuesta = input("Quieres crear otra matriz?(s/n) ")
    


