import pygame as pg
from pygame.locals import *
from game_settings import *
import os

absolute_path = os.path.dirname(__file__)

class Player(pg.sprite.Sprite):
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(absolute_path, "sprite_images/player.png"))
        self.image = pg.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]  
        self.direction = (0, -1)

class Shot(pg.sprite.Sprite):
    speed = 20
    def __init__(self, direction):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(absolute_path, "sprite_images/bullet.png"))
        self.image = pg.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
        self.direction_x, self.direction_y = direction

    def update(self):
        x_speed = self.direction_x * self.speed
        y_speed = self.direction_y * self.speed
        self.rect.move_ip(x_speed, y_speed)
        if (self.rect.y < 0
            or self.rect.y > SCREEN_HEIGHT
            or self.rect.x < 0
            or self.rect.x > SCREEN_WIDTH): self.kill()