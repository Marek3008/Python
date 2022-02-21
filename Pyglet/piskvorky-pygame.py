import pygame, sys

pygame.init()
VYSKA = 600
SIRKA = 600
obrazovka = pygame.display.set_mode((SIRKA, VYSKA))
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            sys.exit()