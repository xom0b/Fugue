import pygame
import sys
import time
import fx
import level
from fx import*
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

        self.TEMPIMAGE = fx(0,0,"images/opacitytest.png",0)

        self.character = char([("images/Animations/Idle/ScarlettIdle1.png", 0.2),("images/Animations/Idle/ScarlettIdle2.png", 0.2),("images/Animations/Idle/ScarlettIdle3.png", 0.2),("images/Animations/Idle/ScarlettIdle4.png", 0.2),("images/Animations/Idle/ScarlettIdle5.png", 0.2),
                                ("images/Animations/Idle/ScarlettNIdle1.png", 0.2),("images/Animations/Idle/ScarlettNIdle2.png", 0.2),("images/Animations/Idle/ScarlettNIdle3.png", 0.2),("images/Animations/Idle/ScarlettNIdle4.png", 0.2),("images/Animations/Idle/ScarlettNIdle5.png", 0.2),
                                ("images/Animations/Run/ScarlettRun1.png", 0.15),("images/Animations/Run/ScarlettRun2.png", 0.15),("images/Animations/Run/ScarlettRun3.png", 0.15),("images/Animations/Run/ScarlettRun4.png", 0.15),("images/Animations/Run/ScarlettRun5.png", 0.15),
                                ("images/Animations/Run/ScarlettRun6.png", 0.15),("images/Animations/Run/ScarlettRun7.png", 0.15),("images/Animations/Run/ScarlettRun8.png", 0.15),("images/Animations/Run/ScarlettRun1_left.png", 0.15),("images/Animations/Run/ScarlettRun2_left.png", 0.15),("images/Animations/Run/ScarlettRun3_left.png", 0.15),("images/Animations/Run/ScarlettRun4_left.png", 0.15),("images/Animations/Run/ScarlettRun5_left.png", 0.15),
                                ("images/Animations/Run/ScarlettRun6_left.png", 0.15),("images/Animations/Run/ScarlettRun7_left.png", 0.15),("images/Animations/Run/ScarlettRun8_left.png", 0.15)],200,200,)

        pygame.mixer.music.load("Theme_1.mp3")
        pygame.mixer.music.play(loops = -1)


        self.ghost=Ghost(self.character,[("images\Animations\Ghost\Ghost1.png",0.2),("images\Animations\Ghost\Ghost2.png",0.2),("images\Animations\Ghost\Ghost3.png",0.2),("images\Animations\Ghost\Ghost4.png",0.2),("images\Animations\Ghost\Ghost5.png",0.2)])
    def menu(self):

        done=False
        while not done:


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                       done=True
            pygame.display.update()
    def quit(self):
        pygame.quit()
        sys.exit()

    def blitAll(self):
        self.D_SURF.blit(self.SURF,(0,0))

        if self.TEMPIMAGE.getAlpha() == 255:
            self.TEMPIMAGE.changeAlpha(5)
        else:
            self.TEMPIMAGE.changeAlpha(-5)
        self.D_SURF.blit(self.TEMPIMAGE.getImage(),(200,200))

    def spritemove(self, pgroup,rgroup,end1,allgroup1,chargroup,dgroup):
        #self.D_SURF.blit(self.character.bg, (self.character.Wx, self.character.Wy))
        for x in pgroup:
            x.move(self.character.Wx, self.character.Wy)
        for x in end1:
            x.move(self.character.Wx, self.character.Wy)
        for x in rgroup:
            x.move(self.character.Wx, self.character.Wy)
        for x in dgroup:
            x.move(self.character.Wx, self.character.Wy)
        allgroup1.draw(self.D_SURF)
        chargroup.draw(self.D_SURF)
        self.character.update()


    def level_0(self):

        CLOCK_0 = pygame.time.Clock()

        LEVEL_0_DONE = False

        #x,y,width,height
        plat1 = plat(0,450,310,10)
        plat2 = plat(310,519,155,10)
        #plat3 = plat(300,450,10,80)
        plat5 = plat(460,595,280,10)
        #plat6 = plat(730,595,10,50)
        plat7 = plat(740,645,120,10)
        plat8 = plat(860,680,200,10)
        plat9 = plat(0,0,10,720)

        end1 = end(990,500, 200, 200, 20, 300)
        enndGroup = pygame.sprite.Group()
        enndGroup.add(end1)

        check1 = rrr(0,0)
        checkGroup = pygame.sprite.Group()
        checkGroup.add(check1)

        deathGroup = pygame.sprite.Group()

        text1 = textZone(30, 400, "They push,we run. Where are they pushing me? What do I do now?")
        tGroup = pygame.sprite.Group(text1)

        currentLevel = level.level(["images/Backgrounds/Intro_1.png", "images/Animations/Run/ScarlettRun1.png"],[],[plat1,plat2,plat5,plat7,plat8,plat9],True)


        R_DOWN = False
        L_DOWN = False


        while not LEVEL_0_DONE:


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
                        self.spritemove(currentLevel.platGroup,checkGroup,enndGroup,currentLevel.platGroup,currentLevel.platGroup,deathGroup)

                    if event.key == pygame.K_SPACE:
                        if self.character.happy:
                            self.character.happy = False
                            currentLevel.toggleState()
                        elif not self.character.happy:
                            self.character.happy = True
                            currentLevel.toggleState()

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




            self.character.bg = currentLevel.currentBackground
            self.character.walls = currentLevel.platGroup
            self.character.end = enndGroup
            self.character.resetgroup = checkGroup
            self.character.textgroup = tGroup
            self.character.deathgroup = deathGroup
            self.spritemove(currentLevel.platGroup,checkGroup,enndGroup,currentLevel.platGroup,currentLevel.platGroup,deathGroup)

            if self.character.checkDeath():
                self.character.restart()
                self.spritemove(currentLevel.platGroup,checkGroup,enndGroup,currentLevel.platGroup,currentLevel.platGroup,deathGroup)


            #BG
            self.D_SURF.blit(currentLevel.currentBackground,(0,0))
            #Platbox
            #currentLevel.drawPlats(self.D_SURF)

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
           # self.character.textgroup.draw(self.D_SURF)
            deathGroup.draw(self.D_SURF)

            print(self.character.resetx, self.character.resety)


            if self.character.level == 1:
                LEVEL_0_DONE = True
                currentLevel.platGroup.empty()





            pygame.display.update()
            CLOCK_0.tick(30)


    def level_1(self):



        CLOCK_1 = pygame.time.Clock()

        LEVEL_1_DONE = False

        plat01 = plat(0, 57, 1020, 30)
        plat02 = plat(0, 309, 324, 99)
        plat03 = plat(324, 408, 253, 94)
        plat04 = plat(577, 502, 130, 776)
        plat05 = plat(707, 1278, 1052, 566)
        plat06 = plat(1860, 1278, 471, 103)
        plat07 = plat(2395, 1312, 47, 67)
        plat08 = plat(2526, 1312, 47, 64)
        plat09 = plat(2646, 1312, 47, 127)
        plat10 = plat(2782, 997, 48, 442)
        plat11 = plat(2310, 945, 472, 52)
        plat12 = plat(2263, 945, 50, 133)
        plat13 = plat(1020, 87, 1093, 995)

        plat14 = plat(708, 606, 93, 49)
        plat15 = plat(708, 883, 93, 49)
        plat16 = plat(926, 1028, 93, 49)
        plat17 = plat(926, 719, 93, 49)

        end2 = end(2694, 1398, 100, 100, 87, 41)

        checkGroup = pygame.sprite.Group()

        enndGroup = pygame.sprite.Group()
        enndGroup.add(end2)

        death1 = death(1760,1356,100,10)
        death2 = death(2331,1393,300,10)
        deathGroup = pygame.sprite.Group()
        deathGroup.add(death1,death2)


        currentLevel = level.level(["images/Backgrounds/Level_1-2 FINAL.png", "images/Backgrounds/Level_1-2 FINAL.png"],[],[plat01,plat02,plat03,plat04,plat05,
                                                                                                                   plat06,plat07,plat08,plat09,plat10,plat11,plat12
                                                                                                                   ,plat13,plat14,plat15,plat16,plat17],True)


        R_DOWN = False
        L_DOWN = False



        while not LEVEL_1_DONE:



            print(self.character.resetx, self.character.resety)

            print(self.character.level)

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
                        self.spritemove(currentLevel.platGroup,checkGroup,enndGroup,currentLevel.platGroup,currentLevel.platGroup,deathGroup)

                    if event.key == pygame.K_SPACE:
                        if self.character.happy:
                            self.character.happy = False
                            currentLevel.toggleState()
                        elif not self.character.happy:
                            self.character.happy = True
                            currentLevel.toggleState()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        R_DOWN = False
                        self.character.right = False

                    elif event.key == pygame.K_LEFT:
                        L_DOWN = False
                        self.character.left = False






            ##NOT ANY OF THIS

            if not self.character.right == self.character.left:
                if self.character.right:
                    self.character.changex = 8
                elif self.character.left:
                    self.character.changex = -8
            else:
                self.character.changex = 0

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




            if self.character.checkDeath():
                self.character.restart()
                self.spritemove(currentLevel.platGroup,checkGroup,enndGroup,currentLevel.platGroup,currentLevel.platGroup,deathGroup)


            #PUT IN GROUP FOR TEXT FOR CHARACTERS
            self.character.bg = currentLevel.currentBackground
            self.character.walls = currentLevel.platGroup
            self.character.end = enndGroup
            self.character.resetgroup = checkGroup
            self.character.deathgroup = deathGroup
            self.spritemove(currentLevel.platGroup,checkGroup,enndGroup,currentLevel.platGroup,currentLevel.platGroup,deathGroup)


            #BG
            self.D_SURF.blit(currentLevel.currentBackground,(self.character.Wx,self.character.Wy))
            #Platbox
            #currentLevel.drawPlats(self.D_SURF)

            #Animation Blit
            self.character.getAnim().blit(self.D_SURF, (self.character.rect.x-17,self.character.rect.y))

            #Text Blit
            self.character.text.drawTo(self.D_SURF)


            if self.character.rect.x > self.ghost.trueX:
                ghostright=False
            else:
                ghostright=True
            if self.character.happy is False:


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

            if self.character.level == 2:
                LEVEL_1_DONE = True



            pygame.display.update()
            CLOCK_1.tick(30)




    def level_2(self):

        self.character.resetx = 50
        self.character.resety = 100

        CLOCK_2 = pygame.time.Clock()

        LEVEL_2_DONE = False

        plat18 = plat(0, 0, 35, 501)
        plat19 = plat(35, 501, 118, 16)
        plat20 = plat(153, 432, 113, 204)
        plat21 = plat(266, 636, 90, 81)
        plat22 = plat(356, 717, 215, 10)
        plat23 = plat(444, 636, 29, 70)
        plat24 = plat(561, 636, 144, 83)
        plat25 = plat(705, 582, 77, 66)
        plat26 = plat(774, 526, 225, 176)
        plat27 = plat(899, 702, 248, 17)
        plat28 = plat(1146, 636, 125, 66)
        plat29 = plat(1271, 702, 82, 10)
        plat30 = plat(1353, 594, 267, 100)
        plat31 = plat(1890, 299, 29, 171)
        plat32 = plat(1575, 300, 59, 170)
        plat33 = plat(1110, 227, 750, 72)
        plat34 = plat(174, 0, 936, 227)
        plat35 = plat(174, 219, 56, 41)
        plat36 = plat(984, 528, 89, 8)
        plat37 = plat(1002, 537, 53, 164)

        end3 = end(1970, 470, 200, 200, 10, 124)




        checkGroup = pygame.sprite.Group()

        enndGroup = pygame.sprite.Group()
        enndGroup.add(end3)

        deathGroup = pygame.sprite.Group()

        death1 = death(358,709,200,10)
        death2 = death(900,645,150,10)
        death3 = death(1221,640,100,10)

        deathGroup.add(death1,death2,death3)


        currentLevel = level.level(["images/Backgrounds/Level_2_Final.png", "images/Backgrounds/Level_2_Final.png"],[],[plat18,plat19,plat20,plat21,plat22,
                                                                                                                   plat23,plat24,plat25,plat26,plat27,plat28,plat29
                                                                                                                   ,plat30,plat31,plat32,plat33,plat34,plat35,plat36,plat37],True)


        R_DOWN = False
        L_DOWN = False



        while not LEVEL_2_DONE:

            print(self.character.resetx, self.character.resety)

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
                        self.spritemove(currentLevel.platGroup,checkGroup,enndGroup,currentLevel.platGroup,currentLevel.platGroup,deathGroup)

                    if event.key == pygame.K_SPACE:
                        if self.character.happy:
                            self.character.happy = False
                            currentLevel.toggleState()
                        elif not self.character.happy:
                            self.character.happy = True
                            currentLevel.toggleState()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        R_DOWN = False
                        self.character.right = False

                    elif event.key == pygame.K_LEFT:
                        L_DOWN = False
                        self.character.left = False






            ##NOT ANY OF THIS

            if not self.character.right == self.character.left:
                if self.character.right:
                    self.character.changex = 8
                elif self.character.left:
                    self.character.changex = -8
            else:
                self.character.changex = 0

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


            if self.character.checkDeath():
                self.character.restart()
                self.spritemove(currentLevel.platGroup,checkGroup,enndGroup,currentLevel.platGroup,currentLevel.platGroup,deathGroup)


            #PUT IN GROUP FOR TEXT FOR CHARACTERS


            self.character.bg = currentLevel.currentBackground
            self.character.walls = currentLevel.platGroup
            self.character.end = enndGroup
            self.character.resetgroup = checkGroup
            self.character.deathgroup = deathGroup
            self.spritemove(currentLevel.platGroup,checkGroup,enndGroup,currentLevel.platGroup,currentLevel.platGroup,deathGroup)


            #BG
            self.D_SURF.blit(currentLevel.currentBackground,(self.character.Wx,self.character.Wy))
            #Platbox
            #currentLevel.drawPlats(self.D_SURF)

            #Animation Blit
            self.character.getAnim().blit(self.D_SURF, (self.character.rect.x-17,self.character.rect.y))

            #Text Blit
            self.character.text.drawTo(self.D_SURF)


            if self.character.rect.x > self.ghost.trueX:
                ghostright=False
            else:
                ghostright=True
            if self.character.happy is False:


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

            if self.character.level == 1:
                self.LEVEL_1_DONE = True


            pygame.display.update()
            CLOCK_2.tick(30)

