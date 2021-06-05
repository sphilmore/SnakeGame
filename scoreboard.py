from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 275)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()



    def update_scoreboard(self):
        self.write(f"ScoreBoard:{self.score}", align= ALIGNMENT, font=(FONT))

    def game_over(self):
        self.goto(0, 0)
        self.write("GameOver", align=ALIGNMENT, font=(FONT))

    def increase_score(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()








