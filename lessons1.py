
import pygame
from pygame.draw import *  #what


pygame.init()
fps = 30
screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption("Моя первая программа")
screen.fill((128, 128, 128)) #background


color_yellow = (225, 225, 0)
color_black = (0, 0, 0)
color_red = (255, 0, 0)

pygame.draw.circle(screen, color_yellow,
                   (300, 200), 100)

pygame.draw.circle(screen, color_black,
                   (300, 200), 100, 1)


pygame.draw.circle(screen, color_red,
                   (250, 190), 25)

pygame.draw.circle(screen, color_black,
                   (250, 190), 25, 1)
pygame.draw.circle(screen, color_black,
                   (250, 190), 10)

pygame.draw.circle(screen, color_red,
                   (350, 190), 20)
pygame.draw.circle(screen, color_black,
                   (350, 190), 20, 1)
pygame.draw.circle(screen, color_black,
                   (350, 190), 10)

pygame.draw.rect(screen, color_black,
                 (260, 250, 80, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = True  #флаг



while finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            finished = False




