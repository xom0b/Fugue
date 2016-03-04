import pygame
from Vector import Vector
from random import *
import pyganim

class Ghost(pygame.sprite.Sprite):
    def randomY(self):
        if randrange(0,4)>2:
            return 720
        else:
            return 0

    def __init__(self, player,Sprites):

        self.right=pyganim.PygAnimation(Sprites[0:4])
        self.left = self.right.getCopy()
        self.left.flip(True, False)
        self.left.makeTransformsPermanent()



        self.left.play()
        self.right.play()

        self.player = player
        self.target = (480, 360)

        self.speed = 0
        self.location=(randrange(-50,1010),self.randomY())
        self.image = pygame.Surface([100, 100])
        self.rect = self.image.get_rect()
        self.trueX = self.location[0]
        self.trueY =self.location[1]
        self.rect.center = self.location
        self.image.fill((255, 255, 255))
        self.on=False



    def getDirection(self, target):

        position = Vector(self.rect.centerx, self.rect.centery)
        target = Vector(target[0], target[1])
        self.distance = target - position

        direction = self.distance.normalize()
        return direction

    def update(self):
        self.target = self.player.rect.center

        self.direction = self.getDirection(self.target)
        if self.direction:
            self.trueX += (self.direction[0] * self.speed)
            self.trueY += (self.direction[1] * self.speed)
            self.rect.center = (round(self.trueX), round(self.trueY))

        if self.on==False:
            self.trueX = self.location[0]
            self.trueY =self.location[1]
            self.rect.center = (round(self.trueX), round(self.trueY))

    def draw(self, screen):
        if self.player.rect.x > self.trueX:
            self.left.blit(screen, self.rect.topleft)
        else:
            self.right.blit(screen,self.rect.topleft)

    
