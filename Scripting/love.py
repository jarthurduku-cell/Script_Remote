import turtle
import random

wn = turtle.Screen()
wn.setup(width=800, height=800)
t = turtle.Turtle()
turtle.bgcolor("black")
t.pensize(3)
t.pencolor("white")

def myPosition(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Letter 'I' drawing
myPosition(-200, 0)
t.forward(60)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(60)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(60)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(270)

myPosition(0, 0)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def hi():
    t.fillcolor('red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

hi()
t.ht()

# Letter 'U' drawing
myPosition(140, 0)
t.left(140)
t.forward(90)
t.left(90)
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(80)
t.right(90)
t.forward(50)
t.right(90)
t.forward(80)
t.left(90)
t.forward(20)
t.left(90)
t.forward(100)

turtle.done()