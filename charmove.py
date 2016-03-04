from charclass import *

pygame.init()
screen = pygame.display.set_mode([800, 800])
clock = pygame.time.Clock()

character = char()
chargroup = pygame.sprite.Group()
chargroup.add(character)
character.highlighted = 0

plat1 = plat(0, 3095, 5615, 40)
plat2 = plat(200, 550, 200, 60)
lwall = plat(0, 0, 10, 3135)
rwall = plat(5615, 0, 10, 3135)
plat3 = plat(0, 700, 100, 100)
end1 = end(1415, 2915, 200, 200)
reset1 = rrr(915, 2500)

allgroup1 = pygame.sprite.Group()

platgroup1 = pygame.sprite.Group()
platgroup1.add(plat1, plat2, lwall, rwall, plat3)
endgroup1 = pygame.sprite.Group()
endgroup1.add(end1)
resetgroup1 = pygame.sprite.Group(reset1)
resetgroup1.add(reset1)
allgroup1.add(plat1, plat2, lwall, rwall, plat3, end1, reset1)


bg1 = pygame.image.load('bfg.jpg').convert()


def menu():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    character.highlighted -= 1
                if event.key == pygame.K_DOWN:
                    character.highlighted += 1
                if event.key == pygame.K_RETURN:
                    if character.level == 0:
                        if character.highlighted == 0:
                            character.level = 1
                        elif character.highlighted == 1:
                            pygame.quit()
                            sys.exit()
    if character.highlighted > 1:
        character.highlighted = 0
    if character.highlighted < 0:
        character.highlighted = 1
    print(character.highlighted)

def spritemove():
    screen.blit(character.bg, (character.Wx, character.Wy))
    if character.level == 1:
        for x in platgroup1:
            x.move(character.Wx, character.Wy)
        end1.move(character.Wx, character.Wy)
        for x in resetgroup1:
            x.move(character.Wx, character.Wy)
        allgroup1.draw(screen)
    chargroup.draw(screen)
    character.update()


def main():
    #Menu Loop
    while character.level == 0:
        menu()

    #Actual Loop
    while True:
        if character.happy:
            screen.fill((0, 255, 0, 0))
        if not character.happy:
            screen.fill((255, 0, 0, 0))

        #print(character.onGround)
        #print(character.happy)
        #print(character.level)
        if character.level == 1:
            character.bg = bg1
            character.walls = platgroup1
            character.end = endgroup1
            character.resetgroup = resetgroup1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    character.right = True
                if event.key == pygame.K_LEFT:
                    character.left = True
                if event.key == pygame.K_UP:
                    if character.onGround == True:
                        character.onGround = False
                        character.changey = -24
                if event.key == pygame.K_SPACE:
                    if character.happy:
                        character.happy = False
                    elif not character.happy:
                        character.happy = True
                if event.key == pygame.K_r:
                    character.restart()
                    spritemove()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    character.right = False
                if event.key == pygame.K_LEFT:
                    character.left = False

        if not character.right == character.left:
            if character.right:
                character.changex = 5
            elif character.left:
                character.changex = -5
        else:
            character.changex = 0

    ###bg move###
        bgw = character.bg.get_width()
        bgh = character.bg.get_height()
        dz_offset = 200
        if character.Wx == 0:
            xlimitL = 0
        else:
            xlimitL = dz_offset
        if character.Wx >= -character.bg.get_width() + screen.get_width():
            xlimitR = screen.get_width() - dz_offset - character.image.get_width()
        else:
            xlimitR = screen.get_width() - character.image.get_width()

        if character.Wy >= 0:
            xlimitU = 0
        else:
            xlimitU = dz_offset
        if character.Wy >= -character.bg.get_height() + screen.get_height() + 60:
            xlimitD = 525 - 105
        else:
            xlimitD = 800 - 105


        if character.rect.x < xlimitL:
            character.rect.x = xlimitL
        if character.rect.x > xlimitR:
            character.rect.x = xlimitR

        if character.rect.y < xlimitU:
            character.rect.y = xlimitU
        if character.rect.y > xlimitD:
            character.rect.y = xlimitD

        if character.rect.y < 0:
            character.rect.y = 0
        if character.rect.y > 800 - 105:
            character.rect.y = 800 - 105

        if character.rect.x == xlimitR:
            character.rect.x = xlimitR - 1
            if character.changex == 5:
                character.Wx -= 5

        if character.rect.x == xlimitL:
            character.rect.x = xlimitL + 1
            if character.changex == -5:
                character.Wx += 5

        if character.rect.y == xlimitD:
            character.rect.y = xlimitD - 1
            character.Wy -= character.changey

        if character.rect.y == xlimitU:
            character.rect.y = xlimitU - 1
            character.Wy -= character.changey


        if character.Wx <= (-bgw - 800 - 75):
            character.Wx = (-bgw - 800 - 75)
        if character.Wx >= 0:
            character.Wx = 0
        if character.Wy <= (-bgh - 800 - 105):
            character.Wy = (-bgh - 800 - 105)
        if character.Wy >= 0:
            character.Wy = 0

        spritemove()
        print(character.resetx, character.resety)






        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__": main()