import pygame
import sys
import sqlite3
from buttonClass import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Flappy Bird")

def get_font(size):
    return pygame.font.SysFont("jueguito\imagenes/font.ttf", size)

BG = pygame.image.load("jueguito\imagenes\Background.png")  # Carga la imagen de fondo

def database():
    # Establecer la conexión con la base de datos
    conexion = sqlite3.connect("datos_jugadores.db")
    cursor = conexion.cursor()

    # Obtener los registros de la base de datos
    cursor.execute("SELECT * FROM jugadores")
    registros = cursor.fetchall()

    # Mostrar los registros en pantalla
    SCREEN.fill("white")

    # Renderizar y mostrar los registros
    y = 100
    for registro in registros:
        nombre = registro[0]
        numero = registro[1]
        texto = f"Nombre: {nombre}, Número: {numero}"
        texto_renderizado = get_font(30).render(texto, True, "black")
        texto_rect = texto_renderizado.get_rect(center=(640, y))
        SCREEN.blit(texto_renderizado, texto_rect)
        y += 50

    # Cerrar la conexión con la base de datos
    conexion.close()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("FLAPPY BIRD", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("jueguito\imagenes\Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        DATABASE_BUTTON = Button(image=pygame.image.load("jueguito\imagenes\Options Rect.png"), pos=(640, 400), 
                            text_input="Base de datos", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("jueguito\imagenes\Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, DATABASE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    from flappyBirdGame import playGame
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if DATABASE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database()

        pygame.display.update()

main_menu()

pygame.quit()
sys.exit()
