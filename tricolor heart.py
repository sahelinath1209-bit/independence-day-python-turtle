import turtle
import math
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)
for scale, color in [(1.0, "orange"), (0.72, "white"), (0.45, "green")]:
    for i in range(120):
        t.penup()
        t.goto(0, 40)
        angle = i * (math.pi * 2) / 120
        x = 16 * (math.sin(angle) ** 3) * 15
        y = (13 * math.cos(angle) - 5 * math.cos(2* angle) - 2 * math.cos(3* angle) - math.cos(4 * angle)) * 15
     #GREEN PART 
        x1 = x* 0.42
        y1 = 40+(y-40)*0.42
        t.color("green")
        t.pendown() 
        t.goto(x1, y1)
      #WHITE PART
        x2 = x* 0.70
        y2 = 40+(y-40)*0.70
        t.color("white")
        t.goto(x2, y2)
   #ORANGE PART
        t.color("orange")
        t.goto(x, y)   
   #START AT THE OUTER END
        for j in range(8):
            t.forward(6)
            t.backward(6) 
            t.right(45)
turtle.done()