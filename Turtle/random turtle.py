import random
import turtle
from turtle import*
from random import randint
t = turtle.Turtle()

colormode(255)

t.pencolor(randint(0,255),randint(0,255),randint(0,255))
dlzka1 = random.randint(20,70)

def stvorec(dlzka):
  for s in range(4):
        t.forward(dlzka)
        t.left(90)
stvorec(dlzka1)

t.penup()
t.goto(randint(-50,200),randint(-50,200))
t.pendown()



t.pencolor(randint(0,255),randint(0,255),randint(0,255))
dlzka2 = random.randint(20,70)

def trojuholnik(dlzka):
    for i in range(3):
      t.forward(dlzka)
      t.left(120)
trojuholnik(dlzka2)

t.penup()
t.goto(randint(-300,300),randint(-300,300))
t.pendown()



t.pencolor(randint(0,255),randint(0,255),randint(0,255))
dlzka3 = random.randint(20,70)

def hexagon(dlzka):
    for h in range(8):
        t.forward(dlzka)
        t.left(45)
hexagon(dlzka3)




#konecne to ide nehehehe :)
