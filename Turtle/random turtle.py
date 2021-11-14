import random
import turtle
from turtle import*
from random import randint
t = turtle.Turtle()
t.hideturtle()
t.speed(15)


t.left(randint(0,360))

colormode(255)

color1 = randint(0,255),randint(0,255),randint(0,255)

t.pencolor(color1)
t.fillcolor(color1)
t.begin_fill()

dlzka1 = random.randint(20,70)

def stvorec(dlzka):
  for s in range(4):
        t.forward(dlzka)
        t.left(90)
stvorec(dlzka1)

t.end_fill()

t.penup()
t.goto(randint(-50,200),randint(-50,200))
t.pendown()

t.left(randint(0,360))

color2 = randint(0,255),randint(0,255),randint(0,255)

t.pencolor(color2)
t.fillcolor(color2)
t.begin_fill()
dlzka2 = random.randint(20,70)

def trojuholnik(dlzka):
    for i in range(3):
      t.forward(dlzka)
      t.left(120)
trojuholnik(dlzka2)

t.end_fill()

t.penup()
t.goto(randint(-300,300),randint(-300,300))
t.pendown()

t.left(randint(0,360))

color3 = randint(0,255),randint(0,255),randint(0,255)

t.pencolor(color3)
t.fillcolor(color3)
t.begin_fill()
dlzka3 = random.randint(20,70)

def hexagon(dlzka):
    for h in range(8):
        t.forward(dlzka)
        t.left(45)
hexagon(dlzka3)

t.end_fill()

t.penup()
t.goto(randint(-500,500),randint(-500,500))
t.pendown()

t.right(randint(0,360))

color4 = randint(0,255),randint(0,255),randint(0,255)
t.pencolor(color4)
t.fillcolor(color4)
t.begin_fill()
dlzka4 = random.randint(20,70)


def kosostvorec(dlzka):
    for m in range(2):
        t.forward(dlzka)
        t.left(70)
        t.forward(dlzka)
        t.left(110)
kosostvorec(dlzka4)

t.end_fill()


turtle.exitonclick()

#konecne to ide nehehehe :)
