import pygame
import sys
from pygame.locals import *

from GhostClass import Ghost
from Player import Player

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():

    pygame.init()
    current_h = 720
    current_w = 960
    size = (current_w, current_h)
    screen = pygame.display.set_mode(size)
    screen.fill(WHITE)
    pygame.display.set_caption("Ghost Demo")

    player = Player((500, 500))
    ghost = Ghost((400, 300), player, 4)
    
    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.move(-5,0)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.move(5,0)
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            player.move(0,-5)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.move(0,5)

        screen.fill(WHITE)
        
        ghost.update()
        player.update()

        ghost.draw(screen)
        player.draw(screen)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__": main()
