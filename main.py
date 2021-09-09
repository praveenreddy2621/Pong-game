import turtle

win = turtle.Screen()
win.title("PONG BY PRAVEEN")
win.bgcolor("green")
win.setup(width=800, height=600)
win.tracer(0)

#score
score_a = 0
score_b = 0


# paddles
pd_a = turtle.Turtle()
pd_a.speed(0)
pd_a.shape("square")
pd_a.shapesize(stretch_len=1, stretch_wid=5)
pd_a.color("black")
pd_a.penup()
pd_a.goto(-350, 0)

pd_b = turtle.Turtle()
pd_b.speed(0)
pd_b.shape("square")
pd_b.shapesize(stretch_len=1, stretch_wid=5)
pd_b.color("black")
pd_b.penup()
pd_b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

#write
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b),align="center",font=("courier",24,"normal"))
# paddle movin

def pd_a_up():
    y = pd_a.ycor()
    y += 20
    pd_a.sety(y)


def pd_a_down():
    y = pd_a.ycor()
    y -= 20
    pd_a.sety(y)


def pd_b_up():
    y = pd_b.ycor()
    y += 20
    pd_b.sety(y)


def pd_b_down():
    y = pd_b.ycor()
    y -= 20
    pd_b.sety(y)


win.listen()
win.onkeypress(pd_a_up, "w")
win.onkeypress(pd_a_down, "s")
win.onkeypress(pd_b_up, "Up")
win.onkeypress(pd_b_down, "Down")

while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    #paddel and ball working
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pd_b.ycor() +40 and ball.ycor() > pd_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pd_a.ycor() +40 and ball.ycor() > pd_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1



