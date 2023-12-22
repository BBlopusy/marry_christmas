import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
s.screensize()
t.width(2)
t.speed(300)

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
s.screensize()  
t.width(1)
t.speed(30)

def snowfall(num_snowflakes):
    t.penup()
    t.hideturtle()
    t.speed(30)
    
    for _ in range(num_snowflakes):
        x = random.randint(-800, 800)
        y = random.randint(-400, 300)
        t.goto(x, y)
        t.dot(random.randint(1, 10), 'white')

col = ('sea green', 'lime', 'green yellow','green')
for i in range(300):
    t.pencolor(col[i%4])
    t.forward(i*4)
    t.right(121)

t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor('red')
font = ("Courier", 90, "bold")
t.write("Merry Christmas!", align="center", font=font)

snowfall(300)
  
s.exitonclick()