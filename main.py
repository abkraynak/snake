import pygame
import time
import constants
import random

pygame.init()
dis = pygame.display.set_mode((constants.WIN_WID, constants.WIN_HGT))
pygame.display.set_caption("Snake")

def printMessage(msg, color):
    font = pygame.font.SysFont(None, 50)
    text = font.render(msg, True, color)
    textRect = text.get_rect(center=(constants.WIN_WID/2, constants.WIN_HGT/2))
    dis.blit(text, textRect)

gameOver = False
gameClose = False
xpos = constants.WIN_WID/2
ypos = constants.WIN_HGT/2
dx = 0
dy = 0
block_xpos = round(random.randrange(0, constants.WIN_WID - constants.BOXSIZE) / 20.0)
block_ypos = round(random.randrange(0, constants.WIN_WID - constants.BOXSIZE) / 20.0)

while not gameOver:
    if gameClose == True:
        dis.fill(constants.WHITE)
        printMessage("Game Over!", constants.RED)
        pygame.display.update()
        time.sleep(3)

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
                gameClose = True
                dx = 0
                dy = 0
    xpos += dx
    ypos += dy
    if xpos >= constants.WIN_WID or xpos < 0 or ypos >= constants.WIN_HGT or ypos < 0:
        gameOver = True
    dis.fill(constants.BLACK)
    pygame.draw.rect(dis, constants.BLUE, [xpos, ypos, constants.BOXSIZE, constants.BOXSIZE])
    pygame.display.update()
    if xpos == block_xpos and ypos == block_ypos:
        print("Block")
    pygame.time.Clock().tick(constants.CLOCK)
pygame.quit()
quit()