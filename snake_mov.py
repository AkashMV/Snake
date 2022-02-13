import turtle

POS_INDICES = [(-40, 0),
               (-20, 0),
               (0, 0)]
MOVE_CONST = 20
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        self.new_l = self.snakes[1:-1]

    def create_snake(self):
        for pos_index in POS_INDICES:
            turt = turtle.Turtle(shape="square")
            turt.color("white")
            turt.pu()
            turt.goto(pos_index)
            self.snakes.append(turt)

    def snake_move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            x_pos = self.snakes[i - 1].xcor()
            y_pos = self.snakes[i - 1].ycor()
            self.snakes[i].goto(x_pos, y_pos)
        self.head.forward(MOVE_CONST)

    def north(self):
        if self.head.heading() != SOUTH:
            self.head.seth(NORTH)

    def east(self):
        if self.head.heading() != WEST:
            self.head.seth(EAST)

    def west(self):
        if self.head.heading() != EAST:
            self.head.seth(WEST)

    def south(self):
        if self.head.heading() != NORTH:
            self.head.seth(SOUTH)

    def wall_collide_check(self):
        if self.head.xcor() > 290 or self.head.xcor() < -295 or self.head.ycor() > 295 or self.head.ycor() < -290:
            return True

    def new_snake(self):
        new_snake = turtle.Turtle()
        new_snake.pu()
        new_snake.shape("square")
        new_snake.goto(self.snakes[-1].pos())
        new_snake.color("black")
        self.snakes.append(new_snake)
        self.new_l.append(new_snake)

    def tail_collide_check(self):
        for i in self.new_l:
            if self.head.distance(i) < 10:
                return True
