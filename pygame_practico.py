import pygame
import random
from matriz import *

matriz = inicializar_matriz(9,9,0)

# --- CONFIGURACIÓN PYGAME ---
pygame.init()
pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sudoku")

NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0, 255, 0)

fondo = pygame.image.load("fondo.sudoku.jpg")
fondo = pygame.transform.scale(fondo, (800, 600))


TAM_CUADRO = 40
MARGEN_X = 200
MARGEN_Y = 100
fuente = pygame.font.Font(None, 40)  # ✅ fuente creada antes del bucle

matriz = inicializar_matriz(9, 9, 0)

# --- BUCLE PRINCIPAL ---
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if 50 <= x <= 250 and 500 <= y <= 550:  # ✅ Botón Reiniciar
                matriz = inicializar_matriz(9, 9, 0)

    pantalla.blit(fondo, (0, 0))

    # --- GRILLA ---
    for i in range(10):
        grosor = 5 if i % 3 == 0 else 1
        pygame.draw.line(pantalla, BLANCO, (MARGEN_X, MARGEN_Y + i * TAM_CUADRO), (MARGEN_X + 9 * TAM_CUADRO, MARGEN_Y + i * TAM_CUADRO),  grosor)
        pygame.draw.line(pantalla, BLANCO, (MARGEN_X + i * TAM_CUADRO, MARGEN_Y),(MARGEN_X + i * TAM_CUADRO, MARGEN_Y + 9 * TAM_CUADRO), grosor)

    # --- MATRIZ ---
    for fila in range(9):
        for col in range(9):
            valor = matriz[fila][col]
            if valor != 0:
                x = MARGEN_X + col * TAM_CUADRO + TAM_CUADRO // 2
                y = MARGEN_Y + fila * TAM_CUADRO + TAM_CUADRO // 2
                texto = fuente.render(str(valor), True, NEGRO)
                texto_rect = texto.get_rect(center=(x, y))
                pantalla.blit(texto, texto_rect)

    # --- BOTONES ---
    botones = {
        "Validar": (550, 500, 200, 50),
        "Reiniciar": (50, 500, 200, 50)
    }
    for texto, coord in botones.items():
        rect = pygame.draw.rect(pantalla, BLANCO, coord)
        texto_render = fuente.render(texto, True, NEGRO)
        pantalla.blit(texto_render, (coord[0] + 20, coord[1] + 10))

    pygame.display.flip()

    
