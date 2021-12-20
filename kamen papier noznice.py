import random
print("VITAJ! MYSLÍŠ SI, ŽE VYHRÁŠ?")
tah = ("kamen", "papier", "noznice")
moje_skore = []
pc_skore = []

def stav():
    print(sum(moje_skore),":", sum(pc_skore))

def kmn_hra():
    while True:
        pc_tah = random.choice(tah)
        moj_tah = input("kamen/papier/noznice:  ")
        print("PC si vybral ",pc_tah)
        if moj_tah == "kamen" and pc_tah == "papier":
            pc_skore.append(1)
            stav()
            False
        if moj_tah == "kamen" and pc_tah == "noznice":
            moje_skore.append(1)
            stav()
            False
        if moj_tah == "kamen" and pc_tah == "kamen":
            pc_skore.append(0)
            moje_skore.append(0)
            stav()
            False
        if moj_tah == "papier" and pc_tah == "kamen":
            moje_skore.append(1)
            stav()
            False
        if moj_tah == "papier" and pc_tah == "noznice":
            pc_skore.append(1)
            stav()
            False
        if moj_tah == "papier" and pc_tah == "papier":
            pc_skore.append(0)
            moje_skore.append(0)
            stav()
            False
        if moj_tah == "noznice" and pc_tah == "kamen":
            pc_skore.append(1)
            stav()
            False
        if moj_tah == "noznice" and pc_tah == "papier":
            moje_skore.append(1)
            stav()
            False
        if moj_tah == "noznice" and pc_tah == "noznice":
            moje_skore.append(0)
            pc_skore.append(0)
            stav()
            False
        if sum(moje_skore) == 3:
            print("Vyhral si! ")
            break
        if sum(pc_skore) == 3:
            print("Pc vyhral! ")
            break
kmn_hra()
