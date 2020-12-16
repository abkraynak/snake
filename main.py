import pygame
import constants

pygame.init()
dis = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Snake")

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

gameOver = False
xpos = 200
ypos = 200
dx = 0
dy = 0

clock = pygame.time.Clock()

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
    xpos += dx
    ypos += dy
    dis.fill(black)
    pygame.draw.rect(dis, blue, [xpos, ypos, constants.BOXSIZE, constants.BOXSIZE])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()