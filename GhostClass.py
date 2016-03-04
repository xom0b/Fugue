import pygame
from Vector import Vector

class Ghost(pygame.sprite.Sprite):

    def __init__(self, location, player, speed):

        self.player = player
        self.target = (480, 360)

        self.speed = speed

        self.image = pygame.Surface([10, 10])
        self.rect = self.image.get_rect()
        self.trueX = location[0]
        self.trueY = location[1]
        self.rect.center = location

        self.image.fill((150, 150, 150))

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

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)

    
