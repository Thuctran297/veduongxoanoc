import turtle
#import math



t=turtle.Turtle()
t.pensize(3)
t.pencolor("black")
t.goto(0,0)
t.speed(100)
count =0
d=0
while True:
    t.pendown()
    t.fd(d)
    d=d+0.1
    t.lt(10)
   
    count+=1
    if count >=200:
        break
turtle.done()