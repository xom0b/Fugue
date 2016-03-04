import pygame
import sys
import time
import fx
import level
from charclass import*
from GhostClass import *
from random import *

class game:
    def __init__(self):
        pygame.init()
        self.DONE = False
        self.W_WIDTH = 960
        self.W_HEIGHT = 720
        self.D_SURF = pygame.display.set_mode((self.W_WIDTH, self.W_HEIGHT), 0, 32)
        self.SURF = pygame.Surface((self.W_WIDTH,self.W_HEIGHT),flags=0,depth=32)
        self.CLOCK = pygame.time.Clock()

        self.TEMPIMAGE = fx.fx(0,0,"images/opacitytest.png",0)

        self.LEVELNUM = 0

        self.character = char([("images/Animations/Idle/ScarlettIdle1.png", 0.2),("images/Animations/Idle/ScarlettIdle2.png", 0.2),("images/Animations/Idle/ScarlettIdle3.png", 0.2),("images/Animations/Idle/ScarlettIdle4.png", 0.2),("images/Animations/Idle/ScarlettIdle5.png", 0.2),
                                ("images/Animations/Idle/ScarlettNIdle1.png", 0.2),("images/Animations/Idle/ScarlettNIdle2.png", 0.2),("images/Animations/Idle/ScarlettNIdle3.png", 0.2),("images/Animations/Idle/ScarlettNIdle4.png", 0.2),("images/Animations/Idle/ScarlettNIdle5.png", 0.2),
                                ("images/Animations/Run/ScarlettRun1.png", 0.15),("images/Animations/Run/ScarlettRun2.png", 0.15),("images/Animations/Run/ScarlettRun3.png", 0.15),("images/Animations/Run/ScarlettRun4.png", 0.15),("images/Animations/Run/ScarlettRun5.png", 0.15),
                                ("images/Animations/Run/ScarlettRun6.png", 0.15),("images/Animations/Run/ScarlettRun7.png", 0.15),("images/Animations/Run/ScarlettRun8.png", 0.15),("images/Animations/Run/ScarlettRun1_left.png", 0.15),("images/Animations/Run/ScarlettRun2_left.png", 0.15),("images/Animations/Run/ScarlettRun3_left.png", 0.15),("images/Animations/Run/ScarlettRun4_left.png", 0.15),("images/Animations/Run/ScarlettRun5_left.png", 0.15),
                                ("images/Animations/Run/ScarlettRun6_left.png", 0.15),("images/Animations/Run/ScarlettRun7_left.png", 0.15),("images/Animations/Run/ScarlettRun8_left.png", 0.15)],200,200,)
        self.ghost=Ghost(self.character,[("images\Animations\Ghost\Ghost1.png",0.2),("images\Animations\Ghost\Ghost2.png",0.2),("images\Animations\Ghost\Ghost3.png",0.2),("images\Animations\Ghost\Ghost4.png",0.2),("images\Animations\Ghost\Ghost5.png",0.2)])

    def quit(self):
        pygame.quit()
        sys.exit()

    def blitAll(self):
        self.D_SURF.blit(self.SURF,(0,0))
        print(self.TEMPIMAGE.getAlpha())
        if self.TEMPIMAGE.getAlpha() == 255:
            self.TEMPIMAGE.changeAlpha(5)
        else:
            self.TEMPIMAGE.changeAlpha(-5)
        self.D_SURF.blit(self.TEMPIMAGE.getImage(),(200,200))

    def spritemove(self, pgroup,rgroup,end1,allgroup1,chargroup):
        self.D_SURF.blit(self.character.bg, (self.character.Wx, self.character.Wy))
        for x in pgroup:
            x.move(self.character.Wx, self.character.Wy)
        for x in end1:
            x.move(self.character.Wx, self.character.Wy)
        for x in rgroup:
            x.move(self.character.Wx, self.character.Wy)
        allgroup1.draw(self.D_SURF)
        chargroup.draw(self.D_SURF)
        self.character.update()



    def playCurrentLevel(self):




        R_DOWN = False
        L_DOWN = False


        while True:

            self.D_SURF.fill((0,0,0,0))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    quit()

                #Keydown

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        R_DOWN = True
                        self.character.right = True

                    elif event.key == pygame.K_LEFT:
                        L_DOWN = True
                        self.character.left = True

                    if event.key == pygame.K_UP:
                        if self.character.onGround == True:
                            self.character.onGround = False
                            self.character.changey = -15

                    if event.key == pygame.K_r:
                        self.character.restart()
                        self.spritemove(self.currentLevel.platGroup,checkGroup,enndGroup,self.currentLevel.platGroup,self.currentLevel.platGroup)

                    if event.key == pygame.K_SPACE:
                        if self.character.happy:
                            self.character.happy = False
                            self.currentLevel.toggleState()
                        elif not self.character.happy:
                            self.character.happy = True
                            self.currentLevel.toggleState()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        R_DOWN = False
                        self.character.right = False

                    elif event.key == pygame.K_LEFT:
                        L_DOWN = False
                        self.character.left = False


            if not self.character.right == self.character.left:
                if self.character.right:
                    self.character.changex = 8
                elif self.character.left:
                    self.character.changex = -8
            else:
                self.character.changex = 0

        ###bg move###

        if not self.character.level == 0:
            bgw = self.character.bg.get_width()
            bgh = self.character.bg.get_height()
            dz_offset = 200
            if self.character.Wx == 0:
                xlimitL = 0
            else:
                xlimitL = dz_offset
            if self.character.Wx >= -self.character.bg.get_width() + self.D_SURF.get_width():
                xlimitR = self.D_SURF.get_width() - dz_offset - self.character.image.get_width()
            else:
                xlimitR = self.D_SURF.get_width() - self.character.image.get_width()

            if self.character.Wy >= 0:
                xlimitU = 0
            else:
                xlimitU = dz_offset
            if self.character.Wy >= -self.character.bg.get_height() + self.D_SURF.get_height():
                xlimitD = 525 - 105
            else:
                xlimitD = 720 - 105


            if self.character.rect.x < xlimitL:
                self.character.rect.x = xlimitL
            if self.character.rect.x > xlimitR:
                self.character.rect.x = xlimitR

            if self.character.rect.y < xlimitU:
                self.character.rect.y = xlimitU
            if self.character.rect.y > xlimitD:
                self.character.rect.y = xlimitD

            if self.character.rect.y < 0:
                self.character.rect.y = 0
            if self.character.rect.y > 720 - 105:
                self.character.rect.y = 720 - 105

            if self.character.rect.x == xlimitR:
                self.character.rect.x = xlimitR - 1
                if self.character.changex == 8:
                    self.character.Wx -= 8

            if self.character.rect.x == xlimitL:
                self.character.rect.x = xlimitL + 1
                if self.character.changex == -8:
                    self.character.Wx += 8

            if self.character.rect.y == xlimitD:
                self.character.rect.y = xlimitD - 1
                self.character.Wy -= self.character.changey

            if self.character.rect.y == xlimitU:
                self.character.rect.y = xlimitU - 1
                self.character.Wy -= self.character.changey


            if self.character.Wx <= (-bgw - 960 - 40):
                self.character.Wx = (-bgw - 960 - 40)
            if self.character.Wx >= 0:
                self.character.Wx = 0
            if self.character.Wy <= (-bgh - 720 - 105):
                self.character.Wy = (-bgh - 720 - 105)
            if self.character.Wy >= 0:
                self.character.Wy = 0


            #ANIMATIONs
            if R_DOWN and not L_DOWN:
                self.character.setAnim('runRight')
                self.character.getAnim().play()

            elif L_DOWN and not R_DOWN:
                self.character.setAnim('runLeft')
                self.character.getAnim().play()


            if R_DOWN == False and L_DOWN == False:
                self.character.setAnim('idle')
                self.character.getAnim().play()





            self.spritemove(self.currentLevel.platGroup,checkGroup,enndGroup,self.currentLevel.platGroup,self.currentLevel.platGroup)


            #BG
            self.D_SURF.blit(self.currentLevel.currentBackground,(self.character.Wx, self.character.Wy))
            #Platbox
            #self.currentLevel.drawPlats(self.D_SURF)

            #Animation Blit
            self.character.getAnim().blit(self.D_SURF, (self.character.rect.x-17,self.character.rect.y))

            #Text Blit
            self.character.text.drawTo(self.D_SURF)

            #end Box
            #enndGroup.draw(self.D_SURF)
            #Collision Box
            #self.D_SURF.blit(self.character.image, (self.character.rect.x, self.character.rect.y))
            ##Ghost on and off
            if self.character.rect.x > self.ghost.trueX:
                ghostright=False
            else:
                ghostright=True
            if self.character.happy is False:

                #self.ghost.location=(randrange(-50,1010),self.ghost.randomY())
                self.ghost.speed=4
                self.ghost.on=True

                if ghostright==True:
                    self.ghost.right.blit(self.D_SURF, self.ghost.rect.topleft)

                else:
                    self.ghost.left.blit(self.D_SURF,self.ghost.rect.topleft)
                    self.ghost.draw(self.D_SURF)


            if self.character.happy is True:
                self.ghost.on=False
                self.ghost.speed=0
                self.ghost.location=(randrange(-50,1010),self.ghost.randomY())
            self.ghost.update()
            self.character.textgroup.draw(self.D_SURF)
            print(self.character.Wx, self.character.Wy)
            pygame.display.update()
            self.CLOCK.tick(30)





    #def reset(self):


    def main(self):

        self.playCurrentLevel()



