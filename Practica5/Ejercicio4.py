from random import *

def crear_tablero_oculto(filas,columnas):
    C0 = "0"  
    matriz = []
    for fil in range(filas):
        matriz.append([0]*columnas)
    for fil in range(filas):
        for col in range(columnas):
            matriz[fil][col] = C0
    return matriz

def crear_tablero_visible(filas,columnas):
    COCULTA = "-"
    matriz = []
    for fil in range(filas):
        matriz.append([0]*columnas)
        
    for fil in range(filas):
        for col in range(columnas):
            matriz[fil][col] = COCULTA
    return matriz

def poner_bombas_tablero_oculto(toculto,bombas):
    CBOMBA = "B"
    
    filas = len(toculto)
    columnas = len(toculto[0])
    
    for fil in range(filas):
        random_fil = randint(1,8)
        random_col = randint(1,8)
        for col in range(columnas):
            toculto[random_fil][random_col] = CBOMBA
    

##def poner_info_tablero_oculto(toculto):
##    C0 = "0"
##    C1 = "1"
##    C2 = "2"
##    C3 = "3"
##    C4 = "4"
##    C5 = "5"
##    C6 = "6"
##    C7 = "7"
##    C8 = "8"
##    CBOMBA = "B"
##    
##    contador = 0
##    filas = len(toculto)-1
##    columnas = len(toculto[0])-1
##
##    #Mirar esquina superior izquierda
##        
##    if toculto[0][0] != CBOMBA:
##        if toculto[0][1] == CBOMBA:
##            contador = contador + 1
##        if toculto[1][0] == CBOMBA:
##            contador = contador + 1
##        if toculto[1][1] == CBOMBA:
##            contador = contador + 1
##            
##    if contador == 1:
##        toculto[0][0] = C1
##    elif contador == 2:
##        toculto[0][0] = C2
##    elif contador == 3:
##        toculto[0][0] = C3
##    elif contador == 4:
##        toculto[0][0] = C4
##    elif contador == 5:
##        toculto[0][0] = C5
##    elif contador == 6:
##        toculto[0][0] = C6
##    elif contador == 7:
##        toculto[0][0] = C7
##    elif contador == 8:
##        toculto[0][0] = C8
##    contador = 0
##
##    
##    #Mirar esquina superior derecha
##    
##    if toculto[0][columnas] != CBOMBA:
##        if toculto[0][columnas-1] == CBOMBA:
##            contador = contador + 1
##        if toculto[1][columnas] == CBOMBA:
##            contador = contador + 1
##        if toculto[1][columnas-1] == CBOMBA:
##            contador = contador + 1
##            
##    if contador == 1:
##        toculto[0][columnas] = C1
##    elif contador == 2:
##        toculto[0][columnas] = C2
##    elif contador == 3:
##        toculto[0][columnas] = C3
##    elif contador == 4:
##        toculto[0][columnas] = C4
##    elif contador == 5:
##        toculto[0][columnas] = C5
##    elif contador == 6:
##        toculto[0][columnas] = C6
##    elif contador == 7:
##        toculto[0][columnas] = C7
##    elif contador == 8:
##        toculto[0][columnas-1] = C8
##    contador = 0
##
##
##    #Mirar esquina inferior izquierda
##
##    if toculto[filas][0] != CBOMBA:
##        if toculto[filas-1][0] == CBOMBA:
##            contador = contador + 1
##        if toculto[filas][1] == CBOMBA:
##            contador = contador + 1
##        if toculto[filas-1][1] == CBOMBA:
##            contador = contador + 1
##            
##    if contador == 1:
##        toculto[filas][0] = C1
##    elif contador == 2:
##        toculto[filas][0] = C2
##    elif contador == 3:
##        toculto[filas][0] = C3
##    elif contador == 4:
##        toculto[filas][0] = C4
##    elif contador == 5:
##        toculto[filas][0] = C5
##    elif contador == 6:
##        toculto[filas][0] = C6
##    elif contador == 7:
##        toculto[filas][0] = C7
##    elif contador == 8:
##        toculto[filas][0] = C8
##    contador = 0
##
##
###Mirar esquina inferior derecha
##
##    if toculto[filas][columnas] != CBOMBA:
##        if toculto[filas-1][columnas] == CBOMBA:
##            contador = contador + 1
##        if toculto[filas][columnas - 1] == CBOMBA:
##            contador = contador + 1
##        if toculto[filas-1][columnas - 1] == CBOMBA:
##            contador = contador + 1
##            
##    if contador == 1:
##        toculto[filas][columnas] = C1
##    elif contador == 2:
##        toculto[filas][columnas] = C2
##    elif contador == 3:
##        toculto[filas][columnas] = C3
##    elif contador == 4:
##        toculto[filas][columnas] = C4
##    elif contador == 5:
##        toculto[filas][columnas] = C5
##    elif contador == 6:
##        toculto[filas][columnas] = C6
##    elif contador == 7:
##        toculto[filas][columnas] = C7
##    elif contador == 8:
##        toculto[filas][columnas] = C8
##    contador = 0
##
##
##    
##    
##    #Mirar dentro de la matriz sin primera y ultima fila y columna
##    
##    for fil in range(1,filas):
##        for col in range(1,columnas):
##            if toculto[fil][col] != CBOMBA:
##                if toculto[fil][col-1] == CBOMBA:
##                    contador = contador + 1
##                    
##                if toculto[fil][col+1] == CBOMBA:
##                    contador = contador + 1
##                    
##                if toculto[fil-1][col] == CBOMBA:
##                    contador = contador + 1
##                    
##                if toculto[fil+1][col] == CBOMBA:
##                    contador = contador + 1
##                    
##                if toculto[fil-1][col-1] == CBOMBA:
##                    contador = contador + 1
##                    
##                if toculto[fil+1][col+1] == CBOMBA:
##                    contador = contador + 1
##                    
##                if toculto[fil-1][col+1] == CBOMBA:
##                    contador = contador + 1
##                    
##                if toculto[fil+1][col-1] == CBOMBA:
##                    contador = contador + 1
##                    
##            if contador == 1:
##                toculto[fil][col] = C1
##            elif contador == 2:
##                toculto[fil][col] = C2
##            elif contador == 3:
##                toculto[fil][col] = C3
##            elif contador == 4:
##                toculto[fil][col] = C4
##            elif contador == 5:
##                toculto[fil][col] = C5
##            elif contador == 6:
##                toculto[fil][col] = C6
##            elif contador == 7:
##                toculto[fil][col] = C7
##            elif contador == 8:
##                toculto[fil][col] = C8
##            contador = 0
##
##            
##
###Mirar fila superior
##    
##    for col in range(1,columnas):
##        if toculto[0][col] != CBOMBA:
##            if toculto[0][col-1] == CBOMBA:
##                    contador = contador + 1
##                    print(contador)
##            if toculto[0][col+1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[1][col-1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[1][col+1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[1][col] == CBOMBA:
##                    contador = contador + 1
##                    
##        if contador == 1:
##            toculto[0][col] = C1
##        elif contador == 2:
##            toculto[0][col] = C2
##        elif contador == 3:
##            toculto[0][col] = C3
##        elif contador == 4:
##            toculto[0][col] = C4
##        elif contador == 5:
##            toculto[0][col] = C5
##        elif contador == 6:
##            toculto[0][col] = C6
##        elif contador == 7:
##            toculto[0][col] = C7
##        elif contador == 8:
##            toculto[0][col] = C8
##        contador = 0
##
###Mirar fila inferior
##    
##    for col in range(1,columnas):
##        if toculto[filas][col] != CBOMBA:
##            if toculto[filas][col-1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[filas][col+1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[filas-1][col-1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[filas-1][col+1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[filas-1][col] == CBOMBA:
##                    contador = contador + 1
##                    
##        if contador == 1:
##            toculto[filas][col] = C1
##        elif contador == 2:
##            toculto[filas][col] = C2
##        elif contador == 3:
##            toculto[filas][col] = C3
##        elif contador == 4:
##            toculto[filas][col] = C4
##        elif contador == 5:
##            toculto[filas][col] = C5
##        elif contador == 6:
##            toculto[filas][col] = C6
##        elif contador == 7:
##            toculto[filas][col] = C7
##        elif contador == 8:
##            toculto[filas][col] = C8
##        contador = 0
##
###Mirar primera columna
##    
##    for fil in range(1,filas):
##        if toculto[fil][0] != CBOMBA:
##            if toculto[fil-1][0] == CBOMBA:
##                    contador = contador + 1
##            if toculto[fil+1][0] == CBOMBA:
##                    contador = contador + 1
##            if toculto[fil-1][1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[fil+1][1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[fil][1] == CBOMBA:
##                    contador = contador + 1
##                    
##        if contador == 1:
##            toculto[fil][0] = C1
##        elif contador == 2:
##            toculto[fil][0] = C2
##        elif contador == 3:
##            toculto[fil][0] = C3
##        elif contador == 4:
##            toculto[fil][0] = C4
##        elif contador == 5:
##            toculto[fil][0] = C5
##        elif contador == 6:
##            toculto[fil][0] = C6
##        elif contador == 7:
##            toculto[fil][0] = C7
##        elif contador == 8:
##            toculto[fil][0] = C8
##        contador = 0
##    
##
##
###Mirar ultima columna
##    
##    for fil in range(1,filas):
##        if toculto[fil][columnas] != CBOMBA:
##            if toculto[fil-1][columnas] == CBOMBA:
##                    contador = contador + 1
##            if toculto[fil-1][columnas-1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[fil][columnas-1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[fil+1][columnas-1] == CBOMBA:
##                    contador = contador + 1
##            if toculto[fil-1][columnas] == CBOMBA:
##                    contador = contador + 1
##                    
##        if contador == 1:
##            toculto[fil-1][columnas] = C1
##        elif contador == 2:
##            toculto[fil-1][columnas] = C2
##        elif contador == 3:
##            toculto[fil-1][columnas] = C3
##        elif contador == 4:
##            toculto[fil-1][columnas] = C4
##        elif contador == 5:
##            toculto[fil-1][columnas] = C5
##        elif contador == 6:
##            toculto[fil-1][columnas] = C6
##        elif contador == 7:
##            toculto[fil-1][columnas] = C7
##        elif contador == 8:
##            toculto[fil-1][columnas] = C8
##        contador = 0

def imprimir_tablero(matriz):
    for fil in range(len(matriz)):
        for col in range(len(matriz)):
            print(matriz[fil][col], end=" ")
        print()


def poner_info_tablero_oculto(toculto):
    C0 = "0"
    C1 = "1"
    C2 = "2"
    C3 = "3"
    C4 = "4"
    C5 = "5"
    C6 = "6"
    C7 = "7"
    C8 = "8"
    CBOMBA = "B"
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
                        
                if contador == 1:
                    contador = C1
                elif contador == 2:
                    contador = C2
                elif contador == 3:
                    contador = C3
                elif contador == 4:
                    contador = C4
                elif contador == 5:
                    contador = C5
                elif contador == 6:
                    contador = C6
                elif contador == 7:
                    contador = C7
                elif contador == 8:
                    contador = C8
                    
                toculto[fil][col] = contador

def tablero_visible_destapar(tvisible, toculto, fila, columna):
    bomba = False
    COCULTA = "-"
    CBOMBA = "B"
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
    CFLAG="F"
    COCULTA = "-"
    CBOMBA = "B"
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
    CFLAG="F"
    CBOMBA = "B"
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

    



filas = 9
columnas = 9
n_bombas = 10

tablero_oculto = crear_tablero_oculto(filas,columnas)
tablero_visible = crear_tablero_visible(filas,columnas)

poner_bombas_tablero_oculto(tablero_oculto,n_bombas)
poner_info_tablero_oculto(tablero_oculto)


#imprimir_tablero(tablero_oculto)
imprimir_tablero(tablero_visible)




####Prueba para Flag.

##fin = True
##
##while fin:
##    fila = int(input("Dame la fila: "))
##    columna = int(input("Dame la columna: "))
##    boleano = input("Dame un True o False: ")
##    numero = tablero_visible_marcar(tablero_visible, fila, columna, boleano)
##    print(numero)
##    imprimir_tablero(tablero_visible)
    


 ####Prueba de encontrar bomba o no.

fin = True
while fin:
    fila = int(input("Dame la fila: "))
    columna = int(input("Dame la columna: "))

    tablero_visible_bomba = tablero_visible_destapar(tablero_visible, tablero_oculto, fila, columna)
    
    if tablero_visible_bomba == False:
        print(tablero_visible_bomba)
        imprimir_tablero(tablero_visible)
    elif tablero_visible_bomba == True:
        print(tablero_visible_bomba)
        print("BOOOOOOOM!")
        fin = False
    else:
        print(tablero_visible_bomba)

