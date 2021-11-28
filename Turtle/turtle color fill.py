import turtle
t = turtle.Turtle()

t.fillcolor("red")
t.begin_fill()

def s(dlzka):
    for i in range(4):
      t.forward(dlzka)
      t.left(90)
s(50)

t.end_fill()

turtle.exitonclick()

