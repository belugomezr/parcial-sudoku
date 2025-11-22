import pygame 
from matriz import *

pygame.init() #iniciliazo pygame

dimension_pantalla = pygame.display.set_mode((800,600)) #Creamos la dimension_pantalla principal (donde vamos a dibujar numeros, sonidos,etc)
pygame.display.set_caption("Mi sudoku") #Titulo de la ventana
fondo = pygame.image.load("fondo.sudoku.jpg") #Cargo la imagen de mi dimension_pantalla 
fondo = pygame.transform.scale(fondo, (800, 600)) #Adapto la imagen a la dimension_pantalla

matriz = [[0 for _ in range(9)] for _ in range(9)]
cargar_numeros(matriz, 45)  # llena la matriz
tablero_inicial = [fila.copy() for fila in matriz]  # números fijos
celda_incorrecta = False
celda_seleccionada = None
puntaje = 0


def dibujar_tablero(pantalla, matriz):
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
    fuente = pygame.font.Font(None, 40)  # tamaño del texto
    tamaño_celdas = 50
    inicio_x = 175
    inicio_y = 75

    for fila in range(9):
        for col in range(9):
            numero = matriz[fila][col]
            if numero != 0:  # solo dibujar los números que existen
                texto = fuente.render(str(numero), True, (0, 0, 0))
                # centrar el número en la celda
                x = inicio_x + col * tamaño_celdas + tamaño_celdas//2 - texto.get_width()//2
                y = inicio_y + fila * tamaño_celdas + tamaño_celdas//2 - texto.get_height()//2
                pantalla.blit(texto, (x, y))

def dibujar_seleccion(pantalla, celda, celda_incorrecta=False):
    if celda:
        fila, col = celda
        color = (255,0,0) if celda_incorrecta else (0,255,0)  # rojo si es error, verde si correcto
        pygame.draw.rect(pantalla, color, (175 + col*50, 75 + fila*50, 50, 50), 3)


while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = evento.pos
            if 175 <= mouseX <= 625 and 75 <= mouseY <= 525:
                fila = (mouseY - 75) // 50
                columna = (mouseX - 175) // 50
                celda_seleccionada = (fila, columna)
                celda_incorrecta = False  # reset cuando seleccionamos otra celda

        elif evento.type == pygame.KEYDOWN and celda_seleccionada:
            fila, col = celda_seleccionada

            # Solo modificar si no es número fijo
            if tablero_inicial[fila][col] == 0:

                if evento.key in (pygame.K_BACKSPACE, pygame.K_DELETE):
                    matriz[fila][col] = 0
                    celda_incorrecta = False

                elif evento.unicode in "123456789":
                    numero = int(evento.unicode)
                    matriz[fila][col] = numero 

                    if validar_numero(matriz, fila, col, numero):
                        celda_incorrecta = False
                        puntaje = actualizar_puntaje(puntaje, matriz, fila, col, numero)
                        print("Puntaje:", puntaje)
                    else:
                        celda_incorrecta = True
                   

    dimension_pantalla.blit(fondo, (0,0))
    dibujar_tablero(dimension_pantalla, matriz)
    dibujar_numeros(dimension_pantalla, matriz)
    dibujar_seleccion(dimension_pantalla, celda_seleccionada, celda_incorrecta)

    pygame.display.update()



# tablero_inicial = []
# for fila in matriz: 
#     tablero_inicial.append(fila.copy())


# celda_seleccionada = None

# tablero_completo = generar_tablero_completo()
# matriz = crear_sudoku_con_pistas(tablero_completo, pistas_por_region=5)


#Bucle principal del juego

# while True:

#     for evento in pygame.event.get():
        
#         #CERRAR VENTANA
#         if evento.type == pygame.QUIT:
#             pygame.quit()
#             quit()
        
    
        
#         # #INGRESAR NUMEROS
#         # if evento.type == pygame.KEYDOWN and celda_seleccionada is not None:
#         #     fila, columna = celda_seleccionada
            
            
#         #     if not casilla_editable(matriz, fila, columna):
#         #         continue


#         #     #NUMEROS DEL 1 AL 9
#         #     if pygame.K_1 <= evento.key <= pygame.K_9:
#         #         numero = evento.key - pygame.K_0
#         #         if es_valido(matriz, fila, columna, numero):
#         #             copia = [fila[:] for fila in matriz]
#         #             copia[fila][columna] = numero

#         #             if resolver_sudoku(copia):  
#         #                 matriz[fila][columna] = numero
#         #             else:
#         #                 print("Ese número hace el sudoku irresoluble")
#         #         else:
#         #             print("Número inválido según reglas")


#         dimension_pantalla.blit(fondo, (0,0))
#         dibujar_tablero(dimension_pantalla)
#         dibujar_numeros(dimension_pantalla, matriz, tablero_inicial)
#         inicializar_matriz(9,9,0)
#         # cargar_numeros(matriz,45)
#         pygame.display.update() #Actualiza