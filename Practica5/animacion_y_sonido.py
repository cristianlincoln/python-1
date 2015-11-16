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
    FPS = 160 
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
    direccion = 'E' # Este
    screen.fill(WHITE)
    while not fin: 
        direccion_anterior = direccion
        if direccion == 'E': # Este
            catx += 5
            if catx+cat_tamx >= PANTANCHO:
                catx -= 5
                direccion = 'S'
        elif direccion == 'S': # Sur
            caty += 5
            if caty+cat_tamy >= PANTALTO:
                caty -= 5
                direccion = 'O'
        elif direccion == 'O': # Oeste
            catx -= 5
            if catx <= 0:
                catx += 5
                direccion = 'N'
        elif direccion == 'N': # Norte
            caty -= 5
            if caty <= 0:
                caty += 5
                direccion = 'E'
        if direccion_anterior != direccion:
            beep.play()
            time.sleep(1) #Hace una 
            #beep.stop()
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
