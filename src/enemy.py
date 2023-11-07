import pygame as pg
from pygame.locals import *
from game_settings import *
import random
import os

absolute_path = os.path.dirname(__file__)

class Enemy(pg.sprite.Sprite):
    speed = 10
    def __init__(self, speed = 10):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(absolute_path, "sprite_images/enemy.png"))
        self.image = pg.transform.scale(self.image, (32, 32))

        mid_x = SCREEN_WIDTH/2
        mid_y = SCREEN_HEIGHT/2
        self.rect = self.image.get_rect()
        if bool(random.getrandbits(1)):
            self.rect.center = (mid_x, random.choice([0, SCREEN_HEIGHT]))
        else:
            self.rect.center = (random.choice([0, SCREEN_WIDTH]), mid_y)

        self.direction = ((mid_x - self.rect.center[0]) / mid_x, 
                     (mid_y - self.rect.center[1]) / mid_y)
        
        self.speed = speed
        
    def update(self):
        movement = (self.direction[0] * self.speed, self.direction[1] * self.speed)
        self.rect.move_ip(*movement)
