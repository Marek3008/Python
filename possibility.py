import random
cisla = (1,2)
random_numbers = random.choice(cisla)

def possibility(number):
    if number == 1:
        print("it's true")
    if number == 2:
        print("it's false")
possibility(random_numbers)
