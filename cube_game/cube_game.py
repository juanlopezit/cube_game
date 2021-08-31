import pygame
import sys
import random


# Constantes

width = 800
height = 600
red_color = (255, 0, 0)
black_color = (0, 0, 0)
blue_color = (0, 0, 255)

# Jugador

player_size = 50
player_pos = [width / 2, height - player_size * 2]

# Enemigos

enemy_size = 50
enemy_pos = [random.randint(0, width - enemy_size), 0]

# Crear ventana

window = pygame.display.set_mode((width, height)) 
game_over = False
clock = pygame.time.Clock()

def collision_detect(player_pos, enemy_pos):
    px = player_pos[0]
    py = player_pos[1]
    ex = enemy_pos[0]
    ey = enemy_pos[1]

    if (ex >= px and ex <(px + player_size)) or (px >= ex and px < (ex + enemy_size)):
        if (ey >= py and ey <(py + player_size)) or (py >= ey and py < (ey + enemy_size)):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= player_size
            if event.key == pygame.K_RIGHT:
                x += player_size

            player_pos[0] = x

    window.fill(black_color)
    if enemy_pos[1] >= 0 and enemy_pos[1] < height:
        enemy_pos[1] += 20
    else:
        enemy_pos[0] = random.randint(0, width - enemy_size)
        enemy_pos[1] = 0
    
    # Colisiones

    if collision_detect(player_pos, enemy_pos):
        game_over = True
        print("Game over!!!")


    # Dibujar enemigo

    pygame.draw.rect(window, blue_color, 
                    (enemy_pos[0], enemy_pos[1], 
                    enemy_size, enemy_size))
        
    # Dibujar jugador

    pygame.draw.rect(window, red_color, (player_pos[0], 
                    player_pos[1], player_size, player_size))
    
    clock.tick(30)
    pygame.display.update()