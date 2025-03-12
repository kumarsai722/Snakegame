import turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
segments=[]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
     #CREATING  A SNAKE BODY   
    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
            segment=turtle.Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    #MOVING THE SNAKE BODY         
    def move(self):
         for i in range(len(self.segments)-1,0,-1):
              new_x=self.segments[i-1].xcor()
              new_y=self.segments[i-1].ycor()
              self.segments[i].goto(new_x,new_y)
         self.segments[0].forward(20)
    def up(self):
       if self.head.heading() != DOWN:
           self.head.setheading(UP) 
    def down(self):
        if self.head.heading() !=UP:
           self.head.setheading(DOWN)
          
    def right(self):
       if self.head.heading() !=LEFT:
           self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    