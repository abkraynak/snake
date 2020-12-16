import pygame
import constants

pygame.init()
dis = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
gameOver = False
xpos = 200
ypos = 200
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
    dis.fill(constants.BLACK)
    pygame.draw.rect(dis, constants.BLUE, [xpos, ypos, constants.BOXSIZE, constants.BOXSIZE])
    pygame.display.update()
    clock.tick(constants.CLOCK)
pygame.quit()
quit()