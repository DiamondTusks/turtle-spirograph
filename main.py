from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()
tim.speed("fastest")
colormode(255)


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.left(gap_size)
        tim.color(random_colour())
        tim.circle(100)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
