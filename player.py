import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # general setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)

        # movement attributes
        self.dirn = pygame.math.Vector2()
        self.pos = pygame.math.Vector2()
        self.speed = 200

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.dirn.y = -1
        elif keys[pygame.K_DOWN]:
            self.dirn.y = 1
        else:
            self.dirn.y = 0

        if keys[pygame.K_RIGHT]:
            self.dirn.x = 1
        elif keys[pygame.K_LEFT]:
            self.dirn.x = -1
        else:
            self.dirn.x = 0
    
    def move(self, dt):
        if self.dirn.magnitude() != 0:
            self.dirn.normalize()

        # horizontal movement
        self.pos.x += self.dirn.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # vertical movement
        self.pos.y += self.dirn.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)
