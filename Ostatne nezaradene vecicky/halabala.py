
def ocekuj(cislo, kto_hra):
    if kto_hra == -1:
        kto_hra = 2
    if cislo % 3 == 0:
        if cislo % 5 == 0:
            print("Hráč ",str(kto_hra),": HalaBala")
        else:
            print("Hráč ",str(kto_hra), ": Hala")
    elif cislo % 5 == 0:
        if cislo % 3 == 0:
            print("Hráč ",str(kto_hra), ": HalaBala")
        else:
            print("Hráč ",str(kto_hra), ": Bala")
    else:
        print("Hráč ",str(kto_hra), ": ", cislo)

n = 1
hrac =  1
while n < 101:
    ocekuj(n, hrac)
    n += 1
    hrac *= -1

    
