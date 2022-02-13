import turtle


class Text(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.color("White")
        self.goto(0, 270)
        self.ht()
        self.score = 0

    def display(self):
        self.write(arg=f"SCORE: {self.score}", align="center", font=("Arial", 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", align="center", font=("Arial", 18, 'normal'))
