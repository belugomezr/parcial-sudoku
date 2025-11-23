import pygame
from matriz import *
from inicio import mostrar_inicio

pygame.init()

# --- Pantalla principal ---
dimension_pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("Mi Sudoku")
fondo = pygame.image.load("fondo.sudoku.jpg")
fondo = pygame.transform.scale(fondo, (800, 600))

# --- FUNCIONES NUEVAS 

def pedir_nick(pantalla):
    fuente = pygame.font.Font(None, 50)
    nick = ""
    escribiendo = True

    while escribiendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nick != "":
                    escribiendo = False
                elif evento.key == pygame.K_BACKSPACE:
                    nick = nick[:-1]
                else:
                    if len(evento.unicode) == 1:
                        nick += evento.unicode

        pantalla.fill((0, 0, 0))
        texto = fuente.render("Ingresá tu Nick:", True, (255, 255, 255))
        pantalla.blit(texto, (200, 200))

        nick_texto = fuente.render(nick, True, (255, 255, 0))
        pantalla.blit(nick_texto, (200, 300))

        pygame.display.update()

    return nick


def guardar_puntaje(nick, puntaje):
    with open("puntajes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nick} - {puntaje}\n")


# --- Mostrar pantalla de inicio ---
accion, nivel = mostrar_inicio()
if accion == "Salir":
    pygame.quit()
    quit()

# --- Definir dificultad ---
if nivel == "Fácil":
    numeros_por_region = 5
elif nivel == "Medio":
    numeros_por_region = 3
elif nivel == "Difícil":
    numeros_por_region = 2
else:
    numeros_por_region = 5  

# --- Crear tablero ---
tablero_inicial = generar_tablero_facil_por_region(numeros_por_region)
matriz = [fila.copy() for fila in tablero_inicial]

celda_incorrecta = False
celda_seleccionada = None
puntaje = 0

# ---------------------- DIBUJOS ------------------------------

def dibujar_tablero(pantalla, matriz):
    color_linea_fina = (200, 200, 200)
    color_linea_gruesa = (0, 0, 0)
    tamaño_celdas = 50
    inicio_x = 175
    inicio_y = 75

    for i in range(10):
        pygame.draw.line(pantalla, color_linea_fina,
                         (inicio_x, inicio_y + i * tamaño_celdas),
                         (inicio_x + tamaño_celdas*9, inicio_y + i * tamaño_celdas), 1)
        pygame.draw.line(pantalla, color_linea_fina,
                         (inicio_x + i * tamaño_celdas, inicio_y),
                         (inicio_x + i * tamaño_celdas, inicio_y + tamaño_celdas*9), 1)

    for i in range(0, 10, 3):
        pygame.draw.line(pantalla, color_linea_gruesa,
                         (inicio_x, inicio_y + i * tamaño_celdas),
                         (inicio_x + tamaño_celdas*9, inicio_y + i * tamaño_celdas), 4)
        pygame.draw.line(pantalla, color_linea_gruesa,
                         (inicio_x + i * tamaño_celdas, inicio_y),
                         (inicio_x + i * tamaño_celdas, inicio_y + tamaño_celdas*9), 4)


def dibujar_numeros(pantalla, matriz):
    fuente = pygame.font.Font(None, 40)
    tamaño_celdas = 50
    inicio_x = 175
    inicio_y = 75

    for fila in range(9):
        for col in range(9):
            numero = matriz[fila][col]
            if numero != 0:
                color = (0,0,0) if tablero_inicial[fila][col] != 0 else (0,0,255)
                texto = fuente.render(str(numero), True, color)
                x = inicio_x + col * tamaño_celdas + tamaño_celdas//2 - texto.get_width()//2
                y = inicio_y + fila * tamaño_celdas + tamaño_celdas//2 - texto.get_height()//2
                pantalla.blit(texto, (x, y))


def dibujar_seleccion(pantalla, celda, celda_incorrecta=False):
    if celda:
        fila, col = celda
        color = (255,0,0) if celda_incorrecta else (0,255,0)
        pygame.draw.rect(pantalla, color, (175 + col*50, 75 + fila*50, 50, 50), 3)


def dibujar_botones(pantalla):
    fuente = pygame.font.Font(None, 40)
    BLANCO = (255,255,255)
    NEGRO = (0,0,0)

    botones = {
        "Validar": pygame.Rect(500, 540, 230, 50),
        "Reiniciar": pygame.Rect(70, 540, 230, 50)
    }

    for texto, rect in botones.items():
        pygame.draw.rect(pantalla, BLANCO, rect)
        texto_render = fuente.render(texto, True, NEGRO)
        pantalla.blit(texto_render, (rect.x + 20, rect.y + 10))

    return botones


# --- Validación del tablero completo ------------------------

def validar_tablero_completo(matriz):
    errores = 0
    for fila in range(9):
        for col in range(9):
            num = matriz[fila][col]
            if num != 0 and not validar_numero(matriz, fila, col, num):
                errores += 1
    return errores

# ------------------- LOOP PRINCIPAL -------------------------

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = evento.pos

            # Selección de celda
            if 175 <= mouseX <= 625 and 75 <= mouseY <= 525:
                fila = (mouseY - 75) // 50
                columna = (mouseX - 175) // 50
                celda_seleccionada = (fila, columna)
                celda_incorrecta = False

            # Botones
            botones = {
                "Validar": pygame.Rect(500, 540, 230, 50),
                "Reiniciar": pygame.Rect(70, 540, 230, 50)
            }

            # --- VALIDAR TABLERO ---
            if botones["Validar"].collidepoint(mouseX, mouseY):
                errores = validar_tablero_completo(matriz)
                puntaje -= errores
                print("Errores:", errores, "Puntaje:", puntaje)

                # PEDIR NICK
                nick = pedir_nick(dimension_pantalla)
                guardar_puntaje(nick, puntaje)

                # VOLVER AL INICIO
                accion, nivel = mostrar_inicio()

                if accion == "Salir":
                    pygame.quit()
                    quit()

                # Ajustar dificultad al volver
                if nivel == "Fácil":
                    numeros_por_region = 5
                elif nivel == "Medio":
                    numeros_por_region = 3
                else:
                    numeros_por_region = 2

                tablero_inicial = generar_tablero_facil_por_region(numeros_por_region)
                matriz = [fila.copy() for fila in tablero_inicial]
                puntaje = 0
                celda_seleccionada = None

            # --- REINICIAR TABLERO ---
            if botones["Reiniciar"].collidepoint(mouseX, mouseY):
                tablero_inicial = generar_tablero_facil_por_region(numeros_por_region)
                matriz = [fila.copy() for fila in tablero_inicial]
                puntaje = 0
                celda_seleccionada = None

        elif evento.type == pygame.KEYDOWN and celda_seleccionada:
            fila, col = celda_seleccionada
            if tablero_inicial[fila][col] == 0:
                if evento.key in (pygame.K_BACKSPACE, pygame.K_DELETE):
                    matriz[fila][col] = 0
                    celda_incorrecta = False
                elif evento.unicode in "123456789":
                    numero = int(evento.unicode)
                    matriz[fila][col] = numero
                    if validar_numero(matriz, fila, col, numero):
                        celda_incorrecta = False
                        puntaje = actualizar_puntaje(puntaje, matriz, fila, col, numero, celda_incorrecta)
                    else:
                        celda_incorrecta = True

    dimension_pantalla.blit(fondo, (0,0))
    dibujar_tablero(dimension_pantalla, matriz)
    dibujar_numeros(dimension_pantalla, matriz)
    dibujar_seleccion(dimension_pantalla, celda_seleccionada, celda_incorrecta)
    dibujar_botones(dimension_pantalla)

    pygame.display.update()
