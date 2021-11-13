import random
import turtle
t = turtle.Turtle()
from random import randint



dlzka1 = random.randint(20,70)

def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)
stvorec(dlzka1)

t.penup()
t.goto(randint(-50,200),randint(-50,200))
t.pendown()

dlzka2 = random.randint(20,70)

def trojuholnik(dlzka):
    for a in range(3):
      t.forward(dlzka)
      t.left(120)
trojuholnik(dlzka2)

t.penup()
t.goto(randint(-300,300),randint(-300,300))
t.pendown()

dlzka3 = random.randint(20,70)


def hexagon(dlzka):
    for b in range(8):
        t.forward(dlzka)
        t.left(45)
hexagon(dlzka3)


turtle.exitonclick()