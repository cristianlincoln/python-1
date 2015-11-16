from random import *

COCULTA = "-"
CFLAG="F"
CBOMBA = "B"
C0 = "0"
C1 = "1"
C2 = "2"
C3 = "3"
C4 = "4"
C5 = "5"
C6 = "6"
C7 = "7"
C8 = "8"



def crear_tablero_oculto(filas,columnas):
      
    matriz = []
    for fil in range(filas):
        matriz.append([C0]*columnas)
    return matriz

#cambiar
def crear_tablero_visible(filas,columnas):
    matriz = []
    for fil in range(filas):
        matriz.append([0]*columnas)
        
    for fil in range(filas):
        for col in range(columnas):
            matriz[fil][col] = COCULTA
    return matriz


def poner_bombas_tablero_oculto(toculto,bombas):
    
    
    filas = len(toculto)
    columnas = len(toculto[0])
    
    for fil in range(filas):
        random_fil = randint(1,8)
        random_col = randint(1,8)
        for col in range(columnas):
            toculto[random_fil][random_col] = CBOMBA
    

def imprimir_tablero(matriz):
    for fil in range(len(matriz)):
        for col in range(len(matriz)):
            print(matriz[fil][col], end=" ")
        print()


def poner_info_tablero_oculto(toculto):
    
    filas = len(toculto)
    columnas = len(toculto[0])
    for fil in range(filas):
        for col in range(columnas):
            if toculto[fil][col] != CBOMBA:
                contador = 0
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
                for caracter in adyacentes:
                    if caracter == "B":
                        contador = contador + 1
                        
                    
                toculto[fil][col] = str(contador)
                

def tablero_visible_destapar(tvisible, toculto, fila, columna):
    bomba = False
    filas = len(toculto)
    columnas = len(toculto[0])

    if fila > filas-1 or columna > columnas-1:
        bomba = None
    elif tvisible[fila][columna] != COCULTA:
        bomba = None
    elif toculto[fila][columna] == CBOMBA:
        bomba = True
    else:
        tvisible[fila][columna] = toculto[fila][columna]
        
    return bomba


def tablero_visible_marcar(tvisible, fila, columna, onoff):
    
    contador = 0 #Al llamar a la función se pone a 0.
    filas = len(tvisible)
    columnas = len(tvisible[0])
    
    if onoff == "True" and fila < filas and columna < columnas:
        tvisible[fila][columna] = CFLAG
        contador = contador + 1
    elif onoff == "False" and fila < filas and columna < columnas:
        tvisible[fila][columna] = COCULTA
        contador = contador - 1
    else:
        return None
    
    return contador


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
