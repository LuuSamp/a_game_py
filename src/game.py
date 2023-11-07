import pygame as pg
from pygame.locals import *
from game_settings import *
from player import Player, Shot
from enemy import Enemy
import random

# Score and other variables
score = 0

def input_handler(event, shots, player):
    '''
    Function to hadle player input
    '''
    if event.key == K_UP: player.direction = (0, -1)
    elif event.key == K_DOWN: player.direction = (0, 1)
    elif event.key == K_LEFT: player.direction = (-1, 0)
    elif event.key == K_RIGHT: player.direction = (1, 0)
    else: return

    shots.add(Shot(player.direction))


def shot_collision(shots, enemies):
    '''
    Function to handle collisions
    '''
    global score
    for enemy in pg.sprite.groupcollide(shots, enemies, True, True):
        enemy.kill()
        score += 1

def enemy_collision(player, enemies):
    for enemy in pg.sprite.spritecollide(player, enemies, False):
        player.kill()

def main():

    pg.init()

    # Initialize groups
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    enemies = pg.sprite.Group()
    shots = pg.sprite.Group()
    player_group = pg.sprite.Group()

    # clock
    clock = pg.time.Clock()

    enemy_cooldown = ENEMY_SPAWN_TIME

    # Initializing sprites
    player = Player()
    player_group.add(player)
    # Enemy() # Created inside sprite group

    enemy_additional_speed = 0

    while player.alive():
        # Event handler
        for event in pg.event.get():
            if event.type == KEYDOWN:
                input_handler(event, shots, player)
            if event.type == QUIT: 
                pg.quit()
                print(f"Final score: {score}")
                exit()

        if enemy_cooldown: 
            enemy_cooldown -= 1
        else: 
            if enemy_additional_speed < ENEMY_SPEED_CAP - Enemy.speed:
                enemy_additional_speed += 1
            enemy_speed = random.randint(Enemy.speed + enemy_additional_speed - 5, Enemy.speed + enemy_additional_speed)
            enemies.add(Enemy(enemy_speed))
            enemy_cooldown = ENEMY_SPAWN_TIME
        
        screen.fill((255, 255, 255))
        shot_collision(shots, enemies)
        enemy_collision(player, enemies)

        enemies.update()
        shots.update()
        player.update()

        player_group.draw(screen)
        enemies.draw(screen)
        shots.draw(screen)

        pg.display.update()

        # Cap framerate
        clock.tick(30)

    print(f"Final score: {score}")

main()