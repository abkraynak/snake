import pygame
import constants

pygame.init()
dis = pygame.display.set_mode((constants.WIN_WID, constants.WIN_HGT))
pygame.display.set_caption("Snake")

gameOver = False
xpos = constants.WIN_WID/2
ypos = constants.WIN_HGT/2
dx = 0
dy = 0

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -constants.BOXSIZE
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = constants.BOXSIZE
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -constants.BOXSIZE
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = constants.BOXSIZE
            elif event.key == pygame.K_q:
                gameOver = True
                dx = 0
                dy = 0
    xpos += dx
    ypos += dy
    if xpos >= constants.WIN_WID or xpos < 0 or ypos >= constants.WIN_HGT or ypos < 0:
        gameOver = True
    dis.fill(constants.BLACK)
    pygame.draw.rect(dis, constants.BLUE, [xpos, ypos, constants.BOXSIZE, constants.BOXSIZE])
    pygame.display.update()
    pygame.time.Clock().tick(constants.CLOCK)
pygame.quit()
quit()