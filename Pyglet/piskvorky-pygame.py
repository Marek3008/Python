import pygame, sys



#toto tu musi byt
pygame.init()

#konstanty a dalsie vecicky
VYSKA = 600
SIRKA = 600
stlacene = False
hrac = 1
vyherca = ""
cas1 = 0

#hracia plocha v terminali
hracia_plocha = [[0,0,0],
[0, 0, 0],
[0, 0, 0]]

#font
font = pygame.font.SysFont("Consolas", 50)
nadpis1 = font.render("VYHRAL HRÁČ 1 !!", True, (102, 204, 51))
nadpis2 = font.render("VYHRAL HRÁČ 2 !!", True, (102, 204, 51))

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




def prida_do_hracej_plochy(riadok, stlpec, cislo, namiesto):
    for riadocek in hracia_plocha:
        for nula in riadocek:
            if nula == 0:
                hracia_plocha[riadok].pop(stlpec)
                hracia_plocha[riadok].insert(stlpec, cislo)

def nakresli_krizik(x1, y1, x2, y2, x3, y3, x4, y4):
    pygame.draw.line(obrazovka, (0, 0, 0), (x1, y1), (x2, y2), 8)
    pygame.draw.line(obrazovka, (0, 0, 0), (x3, y3), (x4, y4), 8)

def nakresli_kruzok(x, y):
    pygame.draw.circle(obrazovka, (0, 0, 0), (x, y), 80, 8)

#######s tymto som maximalne nespokojny ale uz som bol zufaly a nevedel ako mam pokracovat
def nakresli_znak():
    #vlavo hore
    if pozicia_x in range(0, 200) and pozicia_y in range(0, 200):
        if hrac == 1:
            prida_do_hracej_plochy(0, 0, 1, 0)
            nakresli_krizik(20, 20, 180, 180, 180, 20, 20, 180)
        if hrac == -1:
            prida_do_hracej_plochy(0, 0, 2, 0)
            nakresli_kruzok(100, 100)
    #stred hore
    if pozicia_x in range(200, 400) and pozicia_y in range(0, 200):
        if hrac == 1:
            prida_do_hracej_plochy(0, 1, 1, 0)
            nakresli_krizik(220, 20, 380, 180, 380, 20, 220, 180)
        if hrac == -1:
            prida_do_hracej_plochy(0, 1, 2, 0)
            nakresli_kruzok(300, 100)
    #vpravo hore
    if pozicia_x in range(400, 600) and pozicia_y in range(0, 200):
        if hrac == 1:
            prida_do_hracej_plochy(0, 2, 1, 0)
            nakresli_krizik(420, 20, 580, 180, 580, 20, 420, 180)
        if hrac == -1:
            prida_do_hracej_plochy(0, 2, 2, 0)
            nakresli_kruzok(500, 100)
    #vlavo stred
    if pozicia_x in range(0, 200) and pozicia_y in range(200, 400):
        if hrac == 1:
            prida_do_hracej_plochy(1, 0, 1, 0)
            nakresli_krizik(20, 220, 180, 380, 180, 220, 20, 380)
        if hrac == -1:
            prida_do_hracej_plochy(1, 0, 2, 0)
            nakresli_kruzok(100, 300)
    #stred stred
    if pozicia_x in range(200, 400) and pozicia_y in range(200, 400):
        if hrac == 1:
            prida_do_hracej_plochy(1, 1, 1, 0)
            nakresli_krizik(220, 220, 380, 380, 380, 220, 220, 380)
        if hrac == -1:
            nakresli_kruzok(300, 300)
            prida_do_hracej_plochy(1, 1, 2, 0)
    #stred vpravo
    if pozicia_x in range(400, 600) and pozicia_y in range(200, 400):
        if hrac == 1:
            prida_do_hracej_plochy(1, 2, 1, 0)
            nakresli_krizik(420, 220, 580, 380, 580, 220, 420, 380)
        if hrac == -1:
            prida_do_hracej_plochy(1, 2, 2, 0)
            nakresli_kruzok(500, 300)
    #vlavo dole
    if pozicia_x in range(0, 200) and pozicia_y in range(400, 600):
        if hrac == 1:
            prida_do_hracej_plochy(2, 0, 1, 0)
            nakresli_krizik(20, 420, 180, 580, 180, 420, 20, 580)
        if hrac == -1:
            prida_do_hracej_plochy(2, 0, 2, 0)
            nakresli_kruzok(100, 500)
    #stred dole
    if pozicia_x in range(200, 400) and pozicia_y in range(400, 600):
        if hrac == 1:
            prida_do_hracej_plochy(2, 1, 1, 0)
            nakresli_krizik(220, 420, 380, 580, 380, 420, 220, 580)
        if hrac == -1:
            prida_do_hracej_plochy(2, 1, 2, 0)
            nakresli_kruzok(300, 500)
    #vpravo dole
    if pozicia_x in range(400, 600) and pozicia_y in range(400, 600):
        if hrac == 1:
            prida_do_hracej_plochy(2, 2, 1, 0)
            nakresli_krizik(420, 420, 580, 580, 580, 420, 420, 580)
        if hrac == -1:
            prida_do_hracej_plochy(2, 2, 2, 0)
            nakresli_kruzok(500, 500)



def skontroluj_horizontalne():
    #hrac 1
    if hracia_plocha[0] == [1, 1, 1] or hracia_plocha[1] == [1, 1, 1] or hracia_plocha[2] == [1, 1, 1]:
        pygame.draw.line(obrazovka, (204, 51, 0), (15, 100), (585, 100), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca = "1"
    #hrac 2
    if hracia_plocha[0] == [2, 2, 2] or hracia_plocha[1] == [2, 2, 2] or hracia_plocha[2] == [2, 2, 2]:
        pygame.draw.line(obrazovka, (204, 51, 0), (15, 100), (585, 100), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca = "2"
def skontroluj_vertikalne():
    #hrac 1
    if hracia_plocha[0][0] == 1 and hracia_plocha[1][0] == 1 and hracia_plocha[2][0] == 1:
        pygame.draw.line(obrazovka, (204, 51, 0), (100, 15), (100, 585), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca = "1"
    if hracia_plocha[0][1] == 1 and hracia_plocha[1][1] == 1 and hracia_plocha[2][1] == 1:
        pygame.draw.line(obrazovka, (204, 51, 0), (300, 15), (300, 585), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca = "1"
    if hracia_plocha[0][2] == 1 and hracia_plocha[1][2] == 1 and hracia_plocha[2][2] == 1:
        pygame.draw.line(obrazovka, (204, 51, 0), (500, 15), (500, 585), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca = "1"
    #hrac 2
    if hracia_plocha[0][0] == 2 and hracia_plocha[1][0] == 2 and hracia_plocha[2][0] == 2:
        pygame.draw.line(obrazovka, (204, 51, 0), (100, 15), (100, 585), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca = "2"
    if hracia_plocha[0][1] == 2 and hracia_plocha[1][1] == 2 and hracia_plocha[2][1] == 2:
        pygame.draw.line(obrazovka, (204, 51, 0), (300, 15), (300, 585), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca = "2"
    if hracia_plocha[0][2] == 2 and hracia_plocha[1][2] == 2 and hracia_plocha[2][2] == 2:
        pygame.draw.line(obrazovka, (204, 51, 0), (500, 15), (500, 585), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca = "2"
def skontroluj_diagonalne():
    #hrac 1 
    if hracia_plocha[0][0] == 1 and hracia_plocha[1][1] == 1 and hracia_plocha[2][2] == 1:
        pygame.draw.line(obrazovka, (204, 51, 0), (15, 15), (585, 585), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca = "1"
    if hracia_plocha[0][2] == 1 and hracia_plocha[1][1] == 1 and hracia_plocha[2][0] == 1:
        pygame.draw.line(obrazovka, (204, 51, 0), (585, 15), (15, 585), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca = "1"
    #hrac 2
    if hracia_plocha[0][0] == 2 and hracia_plocha[1][1] == 2 and hracia_plocha[2][2] == 2:
        pygame.draw.line(obrazovka, (204, 51, 0), (15, 15), (585, 585), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca = "2"
    if hracia_plocha[0][2] == 2 and hracia_plocha[1][1] == 2 and hracia_plocha[2][0] == 2:
        pygame.draw.line(obrazovka, (204, 51, 0), (585, 15), (15, 585), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca = "2"
    


#hlavny cyklus ktory tu tiez musi byt, v nom je vlastne napisane to co sa ma diat
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT or udalost.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if udalost.type == pygame.MOUSEBUTTONDOWN and stlacene == False :
            stlacene = True
            pozicia = pygame.mouse.get_pos()
            pozicia_x = pozicia[0]
            pozicia_y = pozicia[1]
            nakresli_znak()
            skontroluj_horizontalne()
            skontroluj_vertikalne()
            skontroluj_diagonalne()
        if udalost.type == pygame.MOUSEBUTTONUP and stlacene == True:
            stlacene = False
            hrac *= -1

    pygame.display.update()
