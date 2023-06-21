import pygame
import sys
import random

# Dimensiones de la pantalla
SCREEN_WIDTH = 800  # Ancho de la ventana
SCREEN_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Tamaño y velocidad del jugador
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_X = 100
PLAYER_JUMP_SPEED = 8
PLAYER_GRAVITY = 0.5

# Tamaño y velocidad de los tubos
TUBE_WIDTH = 70
TUBE_GAP = 300  # Espacio vertical entre los tubos
TUBE_SPEED = 4

# Vidas
LIVES = 3

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# Cargar imagen del fondo
background_image = pygame.image.load("jueguito/bg.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
 
# Cargar imagen del avatar
avatar_image = pygame.image.load("jueguito/bird1.png")
avatar_width = 50  # Ancho deseado del avatar
avatar_height = 50  # Alto deseado del avatar
avatar_image = pygame.transform.scale(avatar_image, (avatar_width, avatar_height))

font = pygame.font.Font(None, 36)

def draw_player(player_y):
    screen.blit(avatar_image, (PLAYER_X, player_y))

def draw_tube(tube_x, tube_top_height):
    pygame.draw.rect(screen, GREEN, (tube_x, 0, TUBE_WIDTH, tube_top_height))
    pygame.draw.rect(screen, GREEN, (tube_x, tube_top_height + TUBE_GAP, TUBE_WIDTH, SCREEN_HEIGHT - tube_top_height - TUBE_GAP))

def collision_detection(player_rect, tube_rects):
    for tube_rect in tube_rects:
        if player_rect.colliderect(tube_rect):
            return True
    return False

def game_over():
    pygame.quit()
    sys.exit()

def game_loop():
    player_rect = pygame.Rect(PLAYER_X, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
    tube_rects = []
    score = 0
    lives = LIVES

    player_y = SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
    player_velocity_y = 0 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_velocity_y = -PLAYER_JUMP_SPEED

        screen.fill(WHITE)

        draw_player(player_y)

        if len(tube_rects) == 0 or tube_rects[-1].x < SCREEN_WIDTH - 300:
            tube_center = SCREEN_HEIGHT // 2
            tube_offset = random.randint(-100, 100)
            tube_top_height = tube_center - TUBE_GAP // 2 + tube_offset
            tube_bottom_height = SCREEN_HEIGHT - tube_top_height - TUBE_GAP
            tube_rects.append(pygame.Rect(SCREEN_WIDTH, 0, TUBE_WIDTH, tube_top_height))
            tube_rects.append(pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT - tube_bottom_height, TUBE_WIDTH, tube_bottom_height))
        
        for tube_rect in tube_rects:
            draw_tube(tube_rect.x, tube_rect.height)
            tube_rect.x -= TUBE_SPEED

            if tube_rect.x + TUBE_WIDTH < 0:
                tube_rects.remove(tube_rect)

            if tube_rect.x == PLAYER_X:
                score += 1

        player_velocity_y += PLAYER_GRAVITY
        player_y += player_velocity_y
        player_rect.y = player_y

        if player_y < 0 or player_y + PLAYER_HEIGHT > SCREEN_HEIGHT or collision_detection(player_rect, tube_rects):
            game_over()

        pygame.display.update()
        clock.tick(60)

game_loop()
