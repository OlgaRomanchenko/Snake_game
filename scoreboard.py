from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 23, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()
        self.goto(0, 270)

    def update_scoreboard(self):
        self.write(f" Score {self.score},Hight Score {self.high_score}", align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()