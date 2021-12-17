import random
import turtle
from turtle import*
from random import randint
t = turtle.Turtle()
t.hideturtle()
t.speed(25)
turtle.screensize(canvwidth=3000, canvheight=3000)
"--------------------------------------------------------------"
def after_object():
    t.end_fill()
    t.penup()
    t.goto(randint(-450, 550), randint(-450, 550))
    t.pendown()
    t.left(randint(0,360))
"--------------------------------------------------------------"
def color_filling(actual_color):
    t.pencolor(actual_color)
    t.fillcolor(actual_color)
    t.begin_fill()
"--------------------------------------------------------------"
def stvorec(dlzka):
  for s in range(4):
        t.forward(dlzka)
        t.left(90)
"--------------------------------------------------------------"
def trojuholnik(dlzka):
    for i in range(3):
      t.forward(dlzka)
      t.left(120)
"--------------------------------------------------------------"
def hexagon(dlzka):
    for h in range(8):
        t.forward(dlzka)
        t.left(45)
"--------------------------------------------------------------"
def kosostvorec(dlzka):
    for m in range(2):
        t.forward(dlzka)
        t.left(70)
        t.forward(dlzka)
        t.left(110)
"--------------------------------------------------------------"
colormode(255)

color1 = randint(0, 255), randint(0, 255), randint(0, 255)
color_filling(color1)

dlzka1 = random.randint(20, 70)
stvorec(dlzka1)
after_object()  #after štvorec

color2 = randint(0, 255), randint(0, 255), randint(0, 255)
color_filling(color2)

dlzka2 = random.randint(20, 70)
trojuholnik(dlzka2)
after_object()  #after trojuholník

color3 = randint(0, 255), randint(0, 255), randint(0, 255)
color_filling(color3)

dlzka3 = random.randint(20, 70)
hexagon(dlzka3)
after_object()  #after hexagon

color4 = randint(0, 255), randint(0, 255), randint(0, 255)
color_filling(color4)

dlzka4 = random.randint(30, 90)
kosostvorec(dlzka4)
after_object()

t.end_fill()

turtle.exitonclick()

#konecne to ide nehehehe :)
#neviem ako urobiť náhodný počet objektov :(
