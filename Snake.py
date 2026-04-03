from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.sagments = []
        self.create_snake()
        self.head = self.sagments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.sagments.append(new_segment) 

    def extend(self):
        self.add_segment(self.sagments[-1].position())
        


    def move(self):
            for sag_num in range(len(self.sagments) -1, 0 ,-1):
                new_x = self.sagments[sag_num -1].xcor()
                new_y = self.sagments[sag_num -1].ycor()
                self.sagments[sag_num].goto(new_x, new_y)
            self.head.forward(MOVE_DIST)
    
    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)