import pygame 
from matriz import *

pygame.init() #iniciliazo pygame

dimension_pantalla = pygame.display.set_mode((800,600)) #Creamos la dimension_pantalla principal (donde vamos a dibujar numeros, sonidos,etc)
pygame.display.set_caption("Mi sudoku") #Titulo de la ventana
fondo = pygame.image.load("fondo.sudoku.jpg") #Cargo la imagen de mi dimension_pantalla 
fondo = pygame.transform.scale(fondo, (800, 600)) #Adato la imagen a la dimension_pantalla

matriz = inicializar_matriz(9,9,0)
cargar_numeros(matriz, 45)


#Bucle principal del juego

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    dimension_pantalla.blit(fondo, (0,0))

    pygame.display.update() #Actualiza


    

