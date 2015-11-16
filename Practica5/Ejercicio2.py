# -*- coding: utf-8 -*-

'''
Created on Sep 4, 2013

@author: marcos
'''

import pygame
from pygame.locals import *
import time

# Constantes para la inicialización de la superficie de dibujo
PANTANCHO = 640
PANTALTO = 480
WHITE = (255, 255, 255)

def main():
    # Inicialización de Pygame
    pygame.init()
    # Inicialización de la velocidad de refresco
    FPS = 100 
    fpsClock = pygame.time.Clock()
    # Inicialización de la superficie de dibujo (display surface)
    screen = pygame.display.set_mode((PANTANCHO, PANTALTO))
    pygame.display.set_caption('Gato con animación y sonido')

    # Inicialización del sonido
    beep = pygame.mixer.Sound('beeps.wav')
    # Inicialización de la imagen del gato y de su tamaño
    cat = pygame.image.load('cat.png')
    (cat_tamx, cat_tamy) = cat.get_size()
    # Inicialización de las coordenadas del gato
    catx = 10
    caty = 10
    
    # Bucle principal del juego
    fin = False
    direccion = 'SE' # Este
    screen.fill(WHITE)
    while not fin: 
        direccion_anterior = direccion

        if direccion == 'SE': # SurEste
            catx += 5
            caty += 5
            if catx+cat_tamx >= PANTANCHO:
                catx -=5
                caty -=5
                direccion = 'SO'
            elif caty+cat_tamy >= PANTALTO:
                catx -=5
                caty -=5
                direccion = 'NE'                
        elif direccion == 'NE': # NorEste
            catx += 5
            caty -= 5
            if catx+cat_tamx >= PANTANCHO:
                catx -=5
                caty +=5
                direccion = 'NO'
            elif caty <= 0:  
                catx -=5
                caty +=5
                direccion = 'SE'
        elif direccion == 'NO': # NorOeste
            catx -= 5
            caty -= 5
            if catx <= 0:
                catx +=5
                caty +=5
                direccion = 'NE'
            elif caty <= 0:
                catx +=5
                caty +=5
                direccion = 'SO'            
        elif direccion == 'SO': # SurOeste
            catx -= 5
            caty += 5
            if catx <= 0:
                catx +=5
                caty -=5
                direccion = 'SE'
            elif caty+cat_tamy >= PANTALTO:
                catx +=5
                caty -=5
                direccion = 'NO'
            
        if direccion_anterior != direccion:
            beep.play()
            time.sleep(1) #Hace una parada de un segundo.
            beep.stop()
        # Copiar la imagen del gato a la superficie de dibujo
        screen.fill(WHITE)
        screen.blit(cat, (catx, caty))
        
        # Tratar los eventos (teclado, ratón, etc)
        for event in pygame.event.get():
            if event.type == QUIT:
                fin = True
        # Visualizar en pantalla la superficie de dibujo
        pygame.display.update()
        fpsClock.tick(FPS)
        
    pygame.quit()

if __name__ == '__main__':
    main()
