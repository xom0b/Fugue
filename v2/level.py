import pygame
class level:

    def __init__(self, bg, b_hitboxes ,s_hitboxes ,state):

        self.LIGHTBG = pygame.image.load(bg[0]).convert()
        self.DARKBG = pygame.image.load(bg[1]).convert()
        #True = light
        #False = dark
        self.STATE = state

        self.platGroup = pygame.sprite.Group()
        self.platGroup.add(s_hitboxes)

        self.bigGroup = pygame.sprite.Group()
        self.bigGroup.add(b_hitboxes)


        self.currentBackground = self.LIGHTBG

    def toggleState(self):

        if self.currentBackground == self.LIGHTBG:
            self.currentBackground = self.DARKBG
            self.STATE = False
        else:
            self.currentBackground = self.LIGHTBG
            self.STATE = True

    def drawPlats(self,screen):
        self.platGroup.draw(screen)

    def drawBigPlats(self,screen):
        self.bigGroup.draw(screen)








