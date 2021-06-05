from turtle import Turtle, Screen

starting_position = [(0, 0), (-20, 0), (-40, 0)]
moveing_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segement(position)

    def add_segement(self, position):
        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.segment.append(timmy)

    def extend(self):
        self.add_segement(self.segment[-1].position())


    def move(self):
        for seg_number in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_number - 1].xcor()
            new_y = self.segment[seg_number - 1].ycor()
            self.segment[seg_number].goto(new_x, new_y)
        self.segment[0].forward(moveing_distance)

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
