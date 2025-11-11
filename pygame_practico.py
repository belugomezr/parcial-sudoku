import pygame
import random

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, minimo: int, maximo: int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [random.randint(minimo, maximo)
            for _ in range(cantidad_columnas)]
        matriz.append(fila)
    return matriz

matriz = inicializar_matriz(9, 9, 1, 9)

def mostrar_matriz(matriz:list): 
    for indice in range(len(matriz)):
        for j in range(len(matriz[indice])):
                print(matriz[indice][j], end = " ") 
        print(" ")

mostrar_matriz(matriz)

def dividir_en_regiones(matriz):
    regiones = []
    for fila_inicio in range(0, 9, 3):          # 0, 3, 6
        for col_inicio in range(0, 9, 3):       # 0, 3, 6
            region = [fila[col_inicio:col_inicio+3] for fila in matriz[fila_inicio:fila_inicio+3]]
            regiones.append(region)
    return regiones

regiones = dividir_en_regiones(matriz)
print(regiones)

pygame.init()
pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sudoku")

NEGRO = (0,0,0)
BLANCO = (255,255,255)

fondo = pygame.image.load("parcial-sudoku\\fondo.sudoku.jpg")
fondo = pygame.transform.scale(fondo, (800, 600))
# Tamaño de cada cuadrado
TAM_CUADRO = 40


# Margen inicial para centrar la grilla
MARGEN_X = 200
MARGEN_Y = 100

while True:
    for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
               pygame.quit()
               quit()

    #pantalla.fill((0,0,0))

    color = (255, 255, 255)

    pantalla.blit(fondo, (0, 0))

    #for fila in range(9):
        #for col in range(9):
            #x = MARGEN_X + col * TAM_CUADRO
            #y = MARGEN_Y + fila * TAM_CUADRO
            #pygame.draw.rect(pantalla, BLANCO, (x, y, TAM_CUADRO, TAM_CUADRO), 1)
    for i in range(10):
        grosor = 5 if i % 3 == 0 else 1  # cada 3 líneas, más grueso
    # Líneas horizontales
        pygame.draw.line(pantalla, BLANCO, (MARGEN_X, MARGEN_Y + i * TAM_CUADRO), (MARGEN_X + 9 * TAM_CUADRO, MARGEN_Y + i * TAM_CUADRO),  grosor)
    # Líneas verticales
        pygame.draw.line(pantalla, BLANCO, (MARGEN_X + i * TAM_CUADRO, MARGEN_Y),(MARGEN_X + i * TAM_CUADRO, MARGEN_Y + 9 * TAM_CUADRO), grosor)



    VERDE = (0, 255, 0)
    coordenadas = (30, 30, 130, 70)
    #rectangulo = pygame.draw.rect(pantalla, VERDE, coordenadas)
    fuente = pygame.font.Font(None, 40)
    botones = {
    "Validar": (550, 500, 200, 50),
    "Reiniciar": (50, 500, 200, 50)
    }
    for texto, coord in botones.items():
        rect = pygame.draw.rect(pantalla, BLANCO, coord)
        texto_render = fuente.render(texto, True, NEGRO)
        pantalla.blit(texto_render, (coord[0] + 20, coord[1] + 10))

    pygame.display.flip()

    
