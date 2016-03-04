import pygame
class thoughtText():
    def __init__(self, player):
        self.fadeRate = 0
        self.fadeIn = False
        self.fadeOut = False
        self.fullIn = False
        self.player = player
        self.textWords = "Out, gotta get out!"
        self.font = pygame.font.SysFont("", 30)
        self.image = self.font.render(self.textWords, False, (255, 255, 255))
        self.image.set_alpha(0)
        self.XPOS = player.rect.x + player.image.get_width()
        self.YPOS = player.rect.y - self.image.get_height()

    def update(self):

        self.XPOS = self.player.rect.x + self.player.image.get_width()
        self.YPOS = self.player.rect.y - self.image.get_height()
        if self.fadeIn or self.fadeOut:
            self.image.set_alpha(self.image.get_alpha() + self.fadeRate)

        if self.image.get_alpha() >= 255:
            self.fadeIn = False
            self.fullIn = True
            self.fadeRate = 0
        elif self.image.get_alpha() <= 255:
            self.fadeOut = False
            self.fadeRate = 0
            self.fullIn = False

        else:
            self.fullIn = False

        #if self.player.onGround:
            #self.setFadeIn()
        #else:
            #self.setFadeOut()


       #aprint(self.image.get_alpha())

    def setFadeIn(self):
        self.fadeIn = True
        self.fadeRate = 6

    def setFadeOut(self):
        self.fadeOut = True
        self.fadeRate = -12

    def drawTo(self, blitsurf):
        blitsurf.blit(self.image, (self.XPOS, self.YPOS))

    def changeText(self, newText):
        if newText != self.textWords:
            self.textWords = newText
            self.image = self.font.render(self.textWords, False, (255, 255, 255))
            self.image.set_alpha(0)



