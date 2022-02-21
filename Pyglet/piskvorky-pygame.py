import pygame, sys


#toto tu musi byt
pygame.init()

#konstanty
VYSKA = 600
SIRKA = 600

#obrazovka
obrazovka = pygame.display.set_mode((SIRKA, VYSKA))
obrazovka.fill((93, 173, 226))

#definicia ciar
def ciara(bod_A, bod_B):
    pygame.draw.line(obrazovka, (46, 134, 193), bod_A, bod_B, 10)

#1. vertikalna
ciara((200, 0), (200, 600))
#2. vertikalna
ciara((400, 0), (400, 600))
#1. horizontalna
ciara((0, 200), (600, 200))
#2. horizontalna
ciara((0, 400), (600, 400))

#hlavny cyklus ktory tu tiez musi byt
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()