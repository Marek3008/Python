import random
cisla = (1,2,3)
random_numbers = random.choice(cisla)

def possibility(number):
    if number == 1:
        print(1)
    if number == 2:
        print(2)
    if number == 3:
        print(3)
possibility(random_numbers)


#random choosing numbers. 33% on each number