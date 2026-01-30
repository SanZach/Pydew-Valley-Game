import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((32,64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center = pos)
        #general setup above now below movement attributes to translate keys press
        self.direction = pygame.math.Vector2()      #empty brackets function default value (x=0,y=0)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200        #main speed adjustment change here

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y=0      #so no continuous movement once key pressed
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        print(self.direction)

    def move(self, dt):
        #normalize the vector (direction of vector always 1) as diagonal movement is much faster than any other straight line
        if self.direction.magnitude() > 0:      #as 0,0 can't be normalized
            self.direction = self.direction.normalize()
        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y


    def update(self, dt):
        self.input()
        self.move(dt)

