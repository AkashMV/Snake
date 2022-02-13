import turtle
import time
from snake_mov import Snake
from fooddah import Food
from display import Text

screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("green")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
flag = True


text = Text()

screen.onkey(snake.north, "w")
screen.onkey(snake.east, "d")
screen.onkey(snake.west, "a")
screen.onkey(snake.south, "s")

while flag:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    text.display()
    if food.distance(snake.head) < 15:
        print("Here He comes")
        text.score += 1
        text.clear()
        text.display()
        food.new_pos()
        snake.new_snake()

    if snake.wall_collide_check():
        flag = False
        text.game_over()
        print(snake.head.pos())
    if snake.tail_collide_check():
        flag = False
        text.game_over()



screen.exitonclick()
