import pygame
import sys
import time
import fx
import level
from charclass import*

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


    def playCurrentLevel(self,i_level):



        if i_level == 0:

            self.LEVEL_0_DONE = False
            print("0")

            #x,y,width,height
            plat1 = plat(0,450,310,10)
            plat2 = plat(310,519,155,10)
            #plat3 = plat(300,450,10,80)
            plat5 = plat(460,595,280,10)
            #plat6 = plat(730,595,10,50)
            plat7 = plat(740,645,120,10)
            plat8 = plat(860,680,200,10)
            plat9 = plat(0,0,10,720)

            end1 = end(990,500, 200,200, 20, 300)
            enndGroup = pygame.sprite.Group()
            enndGroup.add(end1)

            check1 = rrr(0,0)
            checkGroup = pygame.sprite.Group()
            checkGroup.add(check1)
            self.currentLevel = level.level(["images/Backgrounds/Intro_1.png", "images/Animations/Run/ScarlettRun1.png"],[],[plat1,plat2,plat5,plat7,plat8,plat9],True)
            self.currentLevel = self.currentLevel

        R_DOWN = False
        L_DOWN = False


        while not self.LEVEL_0_DONE:

            #self.D_SURF.fill((0,0,0,0))

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




            self.character.bg = self.currentLevel.currentBackground
            self.character.walls = self.currentLevel.platGroup
            self.character.end = enndGroup
            self.character.resetgroup = checkGroup
            self.spritemove(self.currentLevel.platGroup,checkGroup,enndGroup,self.currentLevel.platGroup,self.currentLevel.platGroup)


            #BG
            self.D_SURF.blit(self.currentLevel.currentBackground,(0,0))
            #Platbox
            #self.currentLevel.drawPlats(self.D_SURF)

            #Animation Blit
            self.character.getAnim().blit(self.D_SURF, (self.character.rect.x-17,self.character.rect.y))

            #end Box
            #enndGroup.draw(self.D_SURF)
            #Collision Box
            #self.D_SURF.blit(self.character.image, (self.character.rect.x, self.character.rect.y))


            pygame.display.update()
            self.CLOCK.tick(30)





    #def reset(self):


    def main(self):

        self.playCurrentLevel(self.LEVELNUM)



