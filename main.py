import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#CREATING THE SCREEN
t=turtle.Turtle()
screen=turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

    
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on=False
        scoreboard.game_over()
    #DETECT COLLOSION WITH TAIL
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on =False
            scoreboard.game_over()
   










screen.exitonclick()

