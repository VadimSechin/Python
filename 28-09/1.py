import pygame
from pygame.draw import *

pygame.init()


FPS = 30
screen = pygame.display.set_mode((700, 700))
screen.fill((255, 255, 255))

pygame.draw.circle(screen, (255, 255, 51), (350, 350), 100)
pygame.draw.circle(screen, (0, 0, 0), (350, 350), 100, 1)
pygame.draw.circle(screen, (255, 0, 0), (385, 320), 18)
pygame.draw.circle(screen, (0, 0, 0), (385, 320), 18, 1)
pygame.draw.circle(screen, (0, 0, 0), (385, 320), 7)
pygame.draw.circle(screen, (255, 0, 0), (315, 320), 12)
pygame.draw.circle(screen, (0, 0, 0), (315, 320), 12, 1)
pygame.draw.circle(screen, (0, 0, 0), (315, 320), 7)
pygame.draw.line(screen, (0, 0, 0), (310, 400), [390, 400], 15)
pygame.draw.polygon(screen, (0, 0, 0), ((360, 315), (420, 275), (416, 269), (356, 309)))
pygame.draw.polygon(screen, (0, 0, 0), ((330, 316), (280, 276), (286, 270), (336, 310)))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

