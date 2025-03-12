import turtle
class Scoreboard(turtle.Turtle):
   def __init__(self):
       super().__init__()
       self.score=0
       self.color("white")
       self.penup()
       self.goto(0,270)
       self.update_scoreboard()
   def update_scoreboard(self):
        self.write(f"score is {self.score}",align="center",font=("Arial",20,"normal"))

   def increase_score(self):  
        self.score += 1
        self.clear()
        self.update_scoreboard()
   def game_over(self):
       self.goto(0,0)
       self.write(f"Game Over",align="center",font=("Arial",20,"normal"))

       
        