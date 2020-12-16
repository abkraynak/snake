import pygame
import constants

pygame.init()
dis = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Snake")

blue = (0, 0, 255)
red = (255, 0, 0)

print(constants.BOXSIZE)
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
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
    pygame.draw.rect(dis, blue, [200, 200, constants.BOXSIZE, constants.BOXSIZE])
    pygame.display.update()
pygame.quit()
quit()