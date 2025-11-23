import pygame

def mostrar_inicio():
    pantalla = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Sudoku")

    # Cargar fondo
    fondo = pygame.image.load("fondo.sudoku.jpg")
    fondo = pygame.transform.scale(fondo, (800, 600))

    blanco = (255, 255, 255)
    negro = (0,0,0)
    fuente = pygame.font.Font(None, 40)

    # Botones principales
    botones = {
        "Nivel": (300, 200, 200, 50),
        "Jugar": (300, 270, 200, 50),
        "Ver Puntajes": (300, 340, 200, 50),
        "Salir": (300, 410, 200, 50)
    }

    nivel = "Fácil"  # nivel por defecto

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "Salir", nivel

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                mouse_pos = evento.pos
                for texto, coord in botones.items():
                    rect = pygame.Rect(coord)
                    if rect.collidepoint(mouse_pos):
                        if texto == "Jugar":
                            return "Jugar", nivel
                        elif texto == "Nivel":
                            # Cambiar nivel con cada clic
                            if nivel == "Fácil":
                                nivel = "Medio"
                            elif nivel == "Medio":
                                nivel = "Difícil"
                            else:
                                nivel = "Fácil"
                        elif texto == "Ver Puntajes":
                            print("Mostrar puntajes") 
                        elif texto == "Salir":
                            return "Salir", nivel

        # Dibujar fondo y botones
        pantalla.blit(fondo, (0,0))
        for texto, coord in botones.items():
            pygame.draw.rect(pantalla, blanco, coord)
            texto_render = fuente.render(texto, True, negro)
            pantalla.blit(texto_render, (coord[0] + 20, coord[1] + 10))

        # Mostrar nivel actual
        nivel_render = fuente.render(f"Nivel: {nivel}", True, negro)
        pantalla.blit(nivel_render, (300, 150))

        pygame.display.flip()
