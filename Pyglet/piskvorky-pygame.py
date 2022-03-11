import pygame, sys
import random 



#toto tu musi byt
pygame.init()

#konstanty a dalsie vecicky
VYSKA = 700
SIRKA = 600
stlacene = False
hrac = "nikto"
vyherca = []
cas1 = 0
desat_cisel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#hracia plocha v terminali
hracia_plocha = [[0,0,0],
[0, 0, 0],
[0, 0, 0]]

#font
font = pygame.font.SysFont("Consolas", 50)
nadpis1 = font.render("VYHRAL HRÁČ 1 !!", True, (102, 204, 51))
nadpis2 = font.render("VYHRAL HRÁČ 2 !!", True, (102, 204, 51))
remiza1 = font.render("REMÍZA !!", True, (102, 204, 51))
hrac1_text = font.render("Hráč 1", True, (29, 131, 72))
hrac2_text = font.render("Hráč 2", True, (153, 0, 102))

#obrazovka
obrazovka = pygame.display.set_mode((SIRKA, VYSKA))
obrazovka.fill((93, 173, 226))

#ktory hrac zacina
while True:
    nahodne_cislo = random.choice(desat_cisel)
    cislo_hrac1 = int(input("Aké číslo si vybral hráč 1? "))
    cislo_hrac2 = int(input("Aké číslo si vybral hráč 2? "))
    print(nahodne_cislo)
    if cislo_hrac1 - nahodne_cislo > cislo_hrac2 - nahodne_cislo:
        hrac = 1
        print("Začína hráč 1")
        break
    if cislo_hrac2 - nahodne_cislo > cislo_hrac1 - nahodne_cislo:
        hrac = -1
        print("Začína hráč 2")
        break
    if cislo_hrac1 - nahodne_cislo == cislo_hrac2 - nahodne_cislo:
        print("Ideme odznova")
        False

#definicia ciar
def ciara(bod_A, bod_B):
    pygame.draw.line(obrazovka, (46, 134, 193), bod_A, bod_B, 10)

##mriezka
#1. vertikalna
ciara((200, 0), (200, 600))
#2. vertikalna
ciara((400, 0), (400, 600))
#1. horizontalna
ciara((0, 200), (600, 200))
#2. horizontalna
ciara((0, 400), (600, 400))
#spodna
ciara((0, 600), (600, 600))

#texty hracov
obrazovka.blit(hrac1_text, (120, 630))
obrazovka.blit(hrac2_text, (355, 630))


def kto_je_na_rade():
    if hrac == 1:
        pygame.draw.circle(obrazovka, (0, 0, 0), (190, 685), 5)
        pygame.draw.circle(obrazovka, (93, 173, 226), (445, 685), 5)
    if hrac == -1:
        pygame.draw.circle(obrazovka, (0, 0, 0), (445, 685), 5)
        pygame.draw.circle(obrazovka, (93, 173, 226), (190, 685), 5)

#prida kriziky a kruzky do *hracej plochy* vo forme jednotiek a dvojok
def prida_do_hracej_plochy(riadok, stlpec, cislo):
    for riadocek in hracia_plocha:
        for nula in riadocek:
            if nula == 0:
                hracia_plocha[riadok].pop(stlpec)
                hracia_plocha[riadok].insert(stlpec, cislo)

def nakresli_krizik(x1, y1, x2, y2, x3, y3, x4, y4):
    pygame.draw.line(obrazovka, (29, 131, 72), (x1, y1), (x2, y2), 8)
    pygame.draw.line(obrazovka, (29, 131, 72), (x3, y3), (x4, y4), 8)
def nakresli_kruzok(x, y):
    pygame.draw.circle(obrazovka, (153, 0, 102), (x, y), 80, 8)

#######s tymto som maximalne nespokojny ale uz som bol zufaly a nevedel ako mam pokracovat
def nakresli_znak():
    #vlavo hore
    if pozicia_x in range(0, 200) and pozicia_y in range(0, 200):
        if hrac == 1 and hracia_plocha[0][0] == 0:
            prida_do_hracej_plochy(0, 0, 1)
            nakresli_krizik(20, 20, 180, 180, 180, 20, 20, 180)
        if hrac == -1 and hracia_plocha[0][0] == 0:
            prida_do_hracej_plochy(0, 0, 2)
            nakresli_kruzok(100, 100)
    #stred hore
    if pozicia_x in range(200, 400) and pozicia_y in range(0, 200):
        if hrac == 1 and hracia_plocha[0][1] == 0:
            prida_do_hracej_plochy(0, 1, 1)
            nakresli_krizik(220, 20, 380, 180, 380, 20, 220, 180)
        if hrac == -1 and hracia_plocha[0][1] == 0:
            prida_do_hracej_plochy(0, 1, 2)
            nakresli_kruzok(300, 100)
    #vpravo hore
    if pozicia_x in range(400, 600) and pozicia_y in range(0, 200):
        if hrac == 1 and hracia_plocha[0][2] == 0:
            prida_do_hracej_plochy(0, 2, 1)
            nakresli_krizik(420, 20, 580, 180, 580, 20, 420, 180)
        if hrac == -1 and hracia_plocha[0][2] == 0:
            prida_do_hracej_plochy(0, 2, 2)
            nakresli_kruzok(500, 100)
    #vlavo stred
    if pozicia_x in range(0, 200) and pozicia_y in range(200, 400):
        if hrac == 1 and hracia_plocha[1][0] == 0:
            prida_do_hracej_plochy(1, 0, 1)
            nakresli_krizik(20, 220, 180, 380, 180, 220, 20, 380)
        if hrac == -1 and hracia_plocha[1][0] == 0:
            prida_do_hracej_plochy(1, 0, 2)
            nakresli_kruzok(100, 300)
    #stred stred
    if pozicia_x in range(200, 400) and pozicia_y in range(200, 400):
        if hrac == 1 and hracia_plocha[1][1] == 0:
            prida_do_hracej_plochy(1, 1, 1)
            nakresli_krizik(220, 220, 380, 380, 380, 220, 220, 380)
        if hrac == -1 and hracia_plocha[1][1] == 0:
            nakresli_kruzok(300, 300)
            prida_do_hracej_plochy(1, 1, 2)
    #stred vpravo
    if pozicia_x in range(400, 600) and pozicia_y in range(200, 400):
        if hrac == 1 and hracia_plocha[1][2] == 0:
            prida_do_hracej_plochy(1, 2, 1)
            nakresli_krizik(420, 220, 580, 380, 580, 220, 420, 380)
        if hrac == -1 and hracia_plocha[1][2] == 0:
            prida_do_hracej_plochy(1, 2, 2)
            nakresli_kruzok(500, 300)
    #vlavo dole
    if pozicia_x in range(0, 200) and pozicia_y in range(400, 600):
        if hrac == 1 and hracia_plocha[2][0] == 0:
            prida_do_hracej_plochy(2, 0, 1)
            nakresli_krizik(20, 420, 180, 580, 180, 420, 20, 580)
        if hrac == -1 and hracia_plocha[2][0] == 0:
            prida_do_hracej_plochy(2, 0, 2)
            nakresli_kruzok(100, 500)
    #stred dole
    if pozicia_x in range(200, 400) and pozicia_y in range(400, 600):
        if hrac == 1 and hracia_plocha[2][1] == 0:
            prida_do_hracej_plochy(2, 1, 1)
            nakresli_krizik(220, 420, 380, 580, 380, 420, 220, 580)
        if hrac == -1 and hracia_plocha[2][1] == 0:
            prida_do_hracej_plochy(2, 1, 2)
            nakresli_kruzok(300, 500)
    #vpravo dole
    if pozicia_x in range(400, 600) and pozicia_y in range(400, 600):
        if hrac == 1 and hracia_plocha[2][2] == 0:
            prida_do_hracej_plochy(2, 2, 1)
            nakresli_krizik(420, 420, 580, 580, 580, 420, 420, 580)
        if hrac == -1 and hracia_plocha[2][2] == 0:
            prida_do_hracej_plochy(2, 2, 2)
            nakresli_kruzok(500, 500)


# kontroly vyhier
def skontroluj_horizontalne():
    #hrac 1
    if hracia_plocha[0] == [1, 1, 1] or hracia_plocha[1] == [1, 1, 1] or hracia_plocha[2] == [1, 1, 1]:
        pygame.draw.line(obrazovka, (204, 51, 0), (15, 100), (585, 100), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca.append(1)
    #hrac 2
    if hracia_plocha[0] == [2, 2, 2] or hracia_plocha[1] == [2, 2, 2] or hracia_plocha[2] == [2, 2, 2]:
        pygame.draw.line(obrazovka, (204, 51, 0), (15, 300), (585, 300), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca.append(1)
    skontroluj_horizontalne.has_been_called = True
def skontroluj_vertikalne():
    #hrac 1
    if hracia_plocha[0][0] == 1 and hracia_plocha[1][0] == 1 and hracia_plocha[2][0] == 1:
        pygame.draw.line(obrazovka, (204, 51, 0), (100, 15), (100, 585), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca.append(1)
    if hracia_plocha[0][1] == 1 and hracia_plocha[1][1] == 1 and hracia_plocha[2][1] == 1:
        pygame.draw.line(obrazovka, (204, 51, 0), (300, 15), (300, 585), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca.append(1)
    if hracia_plocha[0][2] == 1 and hracia_plocha[1][2] == 1 and hracia_plocha[2][2] == 1:
        pygame.draw.line(obrazovka, (204, 51, 0), (500, 15), (500, 585), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca.append(1)
    #hrac 2
    if hracia_plocha[0][0] == 2 and hracia_plocha[1][0] == 2 and hracia_plocha[2][0] == 2:
        pygame.draw.line(obrazovka, (204, 51, 0), (100, 15), (100, 585), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca.append(1)
    if hracia_plocha[0][1] == 2 and hracia_plocha[1][1] == 2 and hracia_plocha[2][1] == 2:
        pygame.draw.line(obrazovka, (204, 51, 0), (300, 15), (300, 585), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca.append(1)
    if hracia_plocha[0][2] == 2 and hracia_plocha[1][2] == 2 and hracia_plocha[2][2] == 2:
        pygame.draw.line(obrazovka, (204, 51, 0), (500, 15), (500, 585), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca.append(1)
    skontroluj_vertikalne.has_been_called = True
def skontroluj_diagonalne():
    #hrac 1 
    if hracia_plocha[0][0] == 1 and hracia_plocha[1][1] == 1 and hracia_plocha[2][2] == 1:
        pygame.draw.line(obrazovka, (204, 51, 0), (15, 15), (585, 585), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca.append(1)
    if hracia_plocha[0][2] == 1 and hracia_plocha[1][1] == 1 and hracia_plocha[2][0] == 1:
        pygame.draw.line(obrazovka, (204, 51, 0), (585, 15), (15, 585), 12)
        obrazovka.blit(nadpis1, (115, 275))
        vyherca.append(1)
    #hrac 2
    if hracia_plocha[0][0] == 2 and hracia_plocha[1][1] == 2 and hracia_plocha[2][2] == 2:
        pygame.draw.line(obrazovka, (204, 51, 0), (15, 15), (585, 585), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca.append(1)
    if hracia_plocha[0][2] == 2 and hracia_plocha[1][1] == 2 and hracia_plocha[2][0] == 2:
        pygame.draw.line(obrazovka, (204, 51, 0), (585, 15), (15, 585), 12)
        obrazovka.blit(nadpis2, (115, 275))
        vyherca.append(1)
    skontroluj_diagonalne.has_been_called = True
def remiza():
    if 0 not in hracia_plocha[0] and 0 not in hracia_plocha[1] and 0 not in hracia_plocha[2]:
        #if
        obrazovka.blit(remiza1, (200, 275))
        vyherca.append(0)


#kontrolovanie ze ci bola funkcia privolana
skontroluj_horizontalne.has_been_called = False
skontroluj_vertikalne.has_been_called = False
skontroluj_diagonalne.has_been_called = False


#bodka pri hracovi ktory zacina
if hrac == 1:
    pygame.draw.circle(obrazovka, (0, 0, 0), (190, 685), 5)
if hrac  == -1:
    pygame.draw.circle(obrazovka, (0, 0, 0), (445, 685), 5)




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
            if skontroluj_horizontalne.has_been_called == False or skontroluj_vertikalne.has_been_called == False or skontroluj_diagonalne.has_been_called == False:
                remiza()
        if udalost.type == pygame.MOUSEBUTTONUP and stlacene == True:
            stlacene = False
            if pozicia_x in range(0, 600) and pozicia_y in range(0, 600):
                hrac *= -1
            kto_je_na_rade()
            if 1 in vyherca or 0 in vyherca:
                pygame.time.wait(3000)
                pygame.quit()
    pygame.display.update()