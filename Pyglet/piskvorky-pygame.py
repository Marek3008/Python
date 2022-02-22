import pygame, sys



#toto tu musi byt
pygame.init()

#konstanty a dalsie vecicky
VYSKA = 600
SIRKA = 600
stlacene = False
hrac = 1

hracia_plocha = [[0,0,0],
[0, 0, 0],
[0, 0, 0]]


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

#nakresli krizik alebo kruh podla toho ktory hrac je na rade
def nakresli_znaky():
    if hrac == 1:
        pygame.draw.line(obrazovka, (0, 0, 0), (pozicia_x - 80, pozicia_y - 80), (pozicia_x + 80, pozicia_y + 80), 3)
        pygame.draw.line(obrazovka, (0, 0, 0), (pozicia_x + 80, pozicia_y - 80), (pozicia_x - 80, pozicia_y + 80), 3)
    if hrac == -1:
        pygame.draw.circle(obrazovka, (0, 0, 0), (pozicia_x, pozicia_y), 90, 3)


#hlavny cyklus ktory tu tiez musi byt, v nom je vlastne napisane to co sa ma diat
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            sys.exit()
        if udalost.type == pygame.MOUSEBUTTONDOWN and stlacene == False :
            stlacene = True
            print("Stlacene!!")
            pozicia = pygame.mouse.get_pos()
            pozicia_x = pozicia[0]
            pozicia_y = pozicia[1]
            nakresli_znaky()
            print(pozicia)
        if udalost.type == pygame.MOUSEBUTTONUP and stlacene == True:
            stlacene = False
            hrac *= -1
            print(hrac)
    pygame.display.update()