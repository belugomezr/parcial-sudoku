import pygame 
from matriz import *

pygame.init() #iniciliazo pygame

dimension_pantalla = pygame.display.set_mode((800,600)) #Creamos la dimension_pantalla principal (donde vamos a dibujar numeros, sonidos,etc)
pygame.display.set_caption("Mi sudoku") #Titulo de la ventana
fondo = pygame.image.load("fondo.sudoku.jpg") #Cargo la imagen de mi dimension_pantalla 
fondo = pygame.transform.scale(fondo, (800, 600)) #Adapto la imagen a la dimension_pantalla

matriz = inicializar_matriz(9,9,0)
cargar_numeros(matriz, 45)

ANCHO, ALTO = 540, 540 
TAM_CASILLA = ANCHO // 9  # tamaño de cada celda

def dibujar_tablero():
    for i in range(10):
        grosor = 1
        if i % 3 == 0:  # cada 3 líneas, hacer más gruesa
            grosor = 5
        pygame.draw.line(dimension_pantalla, (0,0,0), (0, i*TAM_CASILLA), (ANCHO, i*TAM_CASILLA), grosor)
        pygame.draw.line(dimension_pantalla, (0,0,0), (i*TAM_CASILLA, 0), (i*TAM_CASILLA, ALTO), grosor)


#Bucle principal del juego

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    dimension_pantalla.blit(fondo, (0,0))
    dibujar_tablero()

    pygame.display.update() #Actualiza


    

