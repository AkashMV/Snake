import random
import turtle


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("red")
        self.new_pos()

    def new_pos(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x=x_pos, y=y_pos)
