import pygame, sys
from pygame.locals import *
import pyganim
from thoughttextclass import *


class char(pygame.sprite.Sprite):
    def __init__(self, l_sprites,d_sprites,t_sprites, x, y):
        super().__init__()

        self.light_idle = pyganim.PygAnimation(l_sprites[0:4])
        self.light_runRight = pyganim.PygAnimation(l_sprites[10:18])
        self.light_runLeft = pyganim.PygAnimation(l_sprites[18:28])

        self.dark_idle=pyganim.PygAnimation(d_sprites[0:4])
        self.dark_walkRight=pyganim.PygAnimation(d_sprites[5:])
        self.dark_walkLeft= self.dark_walkRight.getCopy()
        self.dark_walkLeft.flip(True,False)
        self.dark_walkLeft.makeTransformsPermanent()

        self.light2dark=pyganim.PygAnimation(t_sprites[0:6], loop=False)

        self.dark2light=pyganim.PygAnimation(t_sprites[0:6], loop=False)




        self.currentAction = self.light_idle



        #Creates blue rect
        self.image = pygame.Surface([40, 105])
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect()

        #initial x/y
        self.rect.x = x
        self.rect.y = y

        #reset position
        self.resetx = 200
        self.resety = 200


        self.changex = 0
        self.changey = 0
        self.Wx = 0
        self.Wy = 0
        self.g = 1
        self.onGround = False
        self.left = False
        self.right = False
        self.happy = True
        self.level = 0
        self.highlighted = 0
        self.bg = None
        self.text = thoughtText(self)

    def getAnim(self):
        return self.currentAction

    def setAnim(self, action):
        if action == 'idle':
            if self.happy:
                self.currentAction = self.light_idle
            else:
                self.currentAction = self.dark_idle

        if action == 'runRight':
            if self.happy:
                self.currentAction = self.light_runRight
            else:
                self.currentAction = self.dark_walkRight

        if action == 'runLeft':
            if self.happy:
                self.currentAction = self.light_runLeft
            else:
                self.currentAction = self.dark_walkLeft
        if action =='light2dark':
            self.currentAction=self.light2dark
        if action == 'dark2light':
            self.currentAction=self.dark2light


    def update(self):
        self.onGround = False
        self.rect.x += self.changex


        collisionhitlist = pygame.sprite.spritecollide(self, self.walls, False)
        for block in collisionhitlist:
            if self.changex > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.changey += self.g
        if self.changey > 30:
            self.changey = 30
        self.rect.y += self.changey


        collisionhitlist = pygame.sprite.spritecollide(self, self.walls, False)

        for block in collisionhitlist:
            if self.changey > 0:
                self.rect.bottom = block.rect.top
                self.onGround = True


            else:
                self.rect.top = block.rect.bottom
                self.changey = 0

        if self.onGround:
            self.changey = 1
            self.g = 0
        else:
            self.g = 1

        collisionhitlist = pygame.sprite.spritecollide(self, self.end, False)
        for block in collisionhitlist:
            #print("SADF")
            self.level += 1
            self.rect.x = block.newx
            self.rect.y = block.newy
            self.Wx = 0
            self.Wy = 0

        collisionhitlist = pygame.sprite.spritecollide(self, self.resetgroup, False)
        for block in collisionhitlist:
            self.resetx = block.startx
            self.resety = block.starty

        collisionhitlist = pygame.sprite.spritecollide(self, self.textgroup, False)
        for block in collisionhitlist:
            self.text.changeText(block.textName)
            self.text.setFadeIn()



        if len(collisionhitlist) == 0:
            self.text.setFadeOut()


        self.text.update()

    def checkDeath(self):
        collisionhitlist = pygame.sprite.spritecollide(self, self.deathgroup, False)
        for block in collisionhitlist:
            return True



    def restart(self):
        self.rect.x = -self.resetx
        self.rect.y = -self.resety
        if self.rect.x < 200:
            self.rect.x = 200
        if self.rect.y < 200:
            self.rect.y = 200
        # if self.rect.x > 700:
        #     self.rect.x = 700
        # if self.rect.y > 650:
        #     self.rect.y = 650
        self.Wx = -self.resetx + 200
        self.Wy = -self.resety + 200
        self.changex = 0
        self.changey = 0
        self.left = False
        self.right = False


class plat(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((100, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.startx = x
        self.starty = y
    def move(self, m, n):
        self.rect.x = m + self.startx
        self.rect.y = n + self.starty

class end(pygame.sprite.Sprite):
    def __init__(self, x, y, newx, newy, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((200, 100, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.startx = x
        self.starty = y
        self.newx = newx
        self.newy = newy
    def move(self, m, n):
        self.rect.x = m + self.startx
        self.rect.y = n + self.starty

class rrr(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([200, 200])
        self.image.fill((0, 100, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.startx = x
        self.starty = y
    def move(self, m, n):
        self.rect.x = m + self.startx
        self.rect.y = n + self.starty

class death(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.startx = x
        self.starty = y
    def move(self, m, n):
        self.rect.x = m + self.startx
        self.rect.y = n + self.starty

class textZone(pygame.sprite.Sprite):
    def __init__(self, x, y, textname):
        super().__init__()
        self.image = pygame.Surface([200, 200])
        self.image.fill((255, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.startx = x
        self.starty = y
        self.textName = textname

    def move(self, m, n):
        self.rect.x = m + self.startx
        self.rect.y = n + self.starty


