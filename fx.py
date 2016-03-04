import pyganim
import pygame


class fx:

    def __init__(self, xpos, ypos, image, alpha):

        self.XPOS = xpos
        self.YPOS = ypos

        self.image = pygame.image.load(image)
        self.image.set_alpha(alpha)

    def getImage(self):

        return self.image

    def getX(self):

        return self.XPOS

    def getY(self):

        return self.YPOS

    def setX(self, x):

        self.XPOS = x

    def setY(self, y):

        self.YPOS = y

    def changeAlpha(self, rate):
        self.image.set_alpha(self.image.get_alpha()-rate)

    def setAlpha(self, value):
        self.image.set_alpha(value)

    def getAlpha(self):
        return self.image.get_alpha()



