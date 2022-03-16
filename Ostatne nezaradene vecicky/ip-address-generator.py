import random
nieco = []
for i in range(4):
    cislo = random.randint(0, 255)
    nieco.append(cislo)

print(nieco[0], ".", nieco[1], ".", nieco[2], ".", nieco[3])