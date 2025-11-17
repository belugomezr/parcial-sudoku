import pygame 
from matriz import *

pygame.init() #iniciliazo pygame

dimension_pantalla = pygame.display.set_mode((800,600)) #Creamos la dimension_pantalla principal (donde vamos a dibujar numeros, sonidos,etc)
pygame.display.set_caption("Mi sudoku") #Titulo de la ventana
fondo = pygame.image.load("fondo.sudoku.jpg") #Cargo la imagen de mi dimension_pantalla 
fondo = pygame.transform.scale(fondo, (800, 600)) #Adapto la imagen a la dimension_pantalla

matriz = inicializar_matriz(9,9,0)
cargar_numeros(matriz, 45)


def dibujar_tablero(pantalla):
    color_linea_fina = (200, 200, 200)  
    color_linea_gruesa = (0, 0, 0)
    
    tamaño_celdas = 50  #tamaño de cada celda
    inicio_x = 175 #coordenada horizontal
    inicio_y = 75 #coordinada vertical

    # Dibujar las líneas de las celdas (finas)
    for i in range(10):
        # Horizontal
        pygame.draw.line(pantalla, color_linea_fina, 
                         (inicio_x, inicio_y + i * tamaño_celdas), 
                         (inicio_x + tamaño_celdas*9, inicio_y + i * tamaño_celdas), 
                         1)
        # Vertical
        pygame.draw.line(pantalla, color_linea_fina, 
                         (inicio_x + i * tamaño_celdas, inicio_y),
                         (inicio_x + i * tamaño_celdas, inicio_y + tamaño_celdas*9),
                         1)

    # Dibujar líneas gruesas para las regiones
    for i in range(0, 10, 3):
        # Horizontal gruesa
        pygame.draw.line(pantalla, color_linea_gruesa, 
                         (inicio_x, inicio_y + i * tamaño_celdas),
                         (inicio_x + tamaño_celdas*9, inicio_y + i * tamaño_celdas),
                         4)
        # Vertical gruesa
        pygame.draw.line(pantalla, color_linea_gruesa, 
                         (inicio_x + i * tamaño_celdas, inicio_y),
                         (inicio_x + i * tamaño_celdas, inicio_y + tamaño_celdas*9),
                         4)


def dibujar_numeros(pantalla, matriz):
    """
    Dibuja los números de la matriz en la pantalla de Pygame.
    """
    fuente = pygame.font.Font(None, 30)  # tamaño del texto
    tamaño_celdas = 50
    inicio_x = 175
    inicio_y = 75

    for fila in range(9):
        for columna in range(9):
            numero = matriz[fila][columna]
            if numero != 0:  # solo dibujar los números que existen
                texto = fuente.render(str(numero), True, (0, 0, 0))
                # centrar el número en la celda
                x = inicio_x + columna * tamaño_celdas + tamaño_celdas//2 - texto.get_width()//2
                y = inicio_y + fila * tamaño_celdas + tamaño_celdas//2 - texto.get_height()//2
                pantalla.blit(texto, (x, y))

#Bucle principal del juego

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = evento.pos
            if 175 <= mouseX <= 625 and 75 <= mouseY <= 525:
                print(mouseX, mouseY)
                fila = (mouseY - 75) // 50
                columna = (mouseX - 175) // 50
            else:
                celda_seleccionada = None
    
    dimension_pantalla.blit(fondo, (0,0))
    dibujar_tablero(dimension_pantalla)
    dibujar_numeros(dimension_pantalla, matriz)

    pygame.display.update() #Actualiza


    

