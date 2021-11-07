import turtle
t = turtle.Turtle()
"""
def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.right(90)
stvorec(100)


turtle.exitonclick()
"""
"""
def schody():
    for i in range(10):
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.right(90)
schody()
turtle.exitonclick()
"""

def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)
stvorec(40)
t.penup()
t.left(90)
t.forward(150)
t.right(35)
t.pendown()

def stvorec_2(dlzka):
    for a in range(4):
        t.forward(dlzka)
        t.right(90)
stvorec_2(70)

turtle.exitonclick()