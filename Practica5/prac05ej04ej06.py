# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

from random import randint

# Constantes
C0='0'
C1='1'
C2='2'
C3='3'
C4='4'
C5='5'
C6='6'
C7='7'
C8='8'
CBOMBA='B'
CFLAG='F'
COCULTA='-'

def crear_tablero_visible(filas,columnas):
    matriz = []
    for fil in range(filas):
        matriz.append([0]*columnas)
        
    for fil in range(filas):
        for col in range(columnas):
            matriz[fil][col] = COCULTA
    return matriz

def crear_tablero_oculto(filas,columnas):
      
    matriz = []
    for fil in range(filas):
        matriz.append([0]*columnas)
    for fil in range(filas):
        for col in range(columnas):
            matriz[fil][col] = C0
    return matriz

#MIRAR CONTROL BOMBAS
def poner_bombas_tablero_oculto(toculto,bombas):  
    filas = len(toculto)
    columnas = len(toculto[0])
    colocadas = 0
    while colocadas < bombas:
        random_fil =  randint(0,filas-1)
        random_col = randint(0,columnas-1)
        if toculto[random_fil][random_col] != CBOMBA:
            toculto[random_fil][random_col] = CBOMBA
            colocadas += 1


def poner_info_tablero_oculto(toculto):    
    filas = len(toculto)
    columnas = len(toculto[0])
    for fil in range(filas):
        for col in range(columnas):
            if toculto[fil][col] != CBOMBA:
                adyacentes = []
                #Comprobar arriba
                if fil > 0:
                    adyacentes.append(toculto[fil][col])
                    if col > 0:
                        adyacentes.append(toculto[fil-1][col-1])
                    if col < columnas - 1:
                        adyacentes.append(toculto[fil-1][col+1])
                #Comprobar izquierda y derecha
                if col > 0:
                    adyacentes.append(toculto[fil][col-1])
                if col < columnas -1:
                    adyacentes.append(toculto[fil][col+1])
                #Comprobar abajo
                if fil < filas - 1:
                    adyacentes.append(toculto[fil+1][col])
                    if col > 0:
                        adyacentes.append(toculto[fil+1][col-1])
                    if col < columnas -1:
                        adyacentes.append(toculto[fil+1][col+1])
                #Contar en la lista adyacentes las bombas que contiene y colocar en esa posición
                contador = 0
                for caracter in adyacentes:
                    if caracter == CBOMBA:
                        contador = contador + 1
                        
                    
                toculto[fil][col] = str(contador)


def imprimir_tablero(matriz):
    for fil in range(len(matriz)):
        for col in range(len(matriz)):
            print(matriz[fil][col], end=" ")
        print()

def tablero_visible_destapar(tvisible, toculto, fila, columna):
    
    filas = len(toculto)
    columnas = len(toculto[0])

    # Si las coordenadas se salen de rango
    if fila < 0 or fila > filas-1 or \
       columna < 0 or columna > columnas-1:
        bomba = None
    # Si las coordenadas están bien pero la casilla ya está destapada
    elif tvisible[fila][columna] != COCULTA:
        bomba = None
    # Si las coordenadas están bien y la casilla está tapada, pero hay
    # bomba
    elif toculto[fila][columna] == CBOMBA:
        bomba = True
    else:
        tvisible[fila][columna] = toculto[fila][columna]
        bomba = False
        
    return bomba
    
def tablero_visible_marcar(tvisible, fila, columna, onoff):
    
    resultado = 0 
    filas = len(tvisible)
    columnas = len(tvisible[0])

    # Si las coordenadas se salen de rango
    if fila < 0 or fila > filas-1 or \
       columna < 0 or columna > columnas-1:
        bomba = None
    # Si las coordenadas están bien e intenta marcar una casilla
    # que no está marcada
    elif onoff==True and tvisible[fila][columna] == COCULTA:
        tvisible[fila][columna] = CFLAG
        resultado = 1
    # Si las coordenadas están bien e intenta marcar una casilla
    # que no está marcada
    elif onoff==False and tvisible[fila][columna] == CFLAG:
        tvisible[fila][columna] = COCULTA
        resultado = -1
    else:
        return None
    
    return resultado

def comprobar_tablero_visible(tvisible, toculto, bombas):
    contador = 0
    filas = len(tvisible)
    columnas = len(tvisible[0])
    for fil in range(filas):
        for col in range(columnas):
            if tvisible[fil][col] == toculto[fil][col]:
                if tvisible[fil][col] == CBOMBA:
                    contador = contador + 1
    if contador == bombas:
        return True
    else:
        return False

def menu_buscaminas():
    opcion = 0
    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
        print ("(1) Destapar casilla")
        print ("(2) Marcar casilla")
        print ("(3) Desmarcar casilla")
        print ("(4) Bombas por detectar")
        print ("(5) Salir")
        opcion = int(input("Elige opción: "))
    return opcion
    
def main():
    seguir  = True
    fin = True
    while fin:
        nivel = input("Dame el nivel de dificultad: ")
        if nivel == "E":
            filas = 8
            columnas = 8
            n_bombas = 10
            fin = False
        elif nivel == "M":
            filas = 16
            columnas = 16
            n_bombas = 40
            fin = False
        elif nivel == "H":
            filas = 16
            columnas = 36
            n_bombas = 99
            fin = False
        else:
            print("No es una opcion valida!")

    
    tablero_oculto = crear_tablero_oculto(filas,columnas)
    tablero_visible = crear_tablero_visible(filas,columnas)
    poner_bombas_tablero_oculto(tablero_oculto,n_bombas)
    poner_info_tablero_oculto(tablero_oculto)
    imprimir_tablero(tablero_visible)
    
    opcion = menu_buscaminas()
    while opcion != 5 and seguir:
        if opcion == 1:
            fila = int(input("Dame la fila: "))
            columna = int(input("Dame la columna: "))
            resultado = tablero_visible_destapar(tablero_visible, tablero_oculto, fila, columna)
            if resultado == None:
                print("Movimiento no valido!!")
            elif resultado == True:
                print("BOOM!!")
                seguir = False
        if opcion == 2 and seguir:
            resultado = 0
            fila = int(input("Dame la fila: "))
            columna = int(input("Dame la columna: "))
            boleano = True
            numero = tablero_visible_marcar(tablero_visible, fila, columna, boleano)
            #Contar numero de aciertos para comprobar si se han marcado todos.
            resultado = resultado + numero
            

        if opcion == 3 and seguir:
            fila = int(input("Dame la fila: "))
            columna = int(input("Dame la columna: "))
            boleano = True
            numero = tablero_visible_marcar(tablero_visible, fila, columna, boleano)
        imprimir_tablero(tablero_visible)
        opcion = menu_buscaminas()
            
        
    


# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__ == "__main__":
    main()
