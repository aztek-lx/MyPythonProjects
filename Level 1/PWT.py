import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("skyblue")
t.penup()
t.pencolor("red")

t.goto(-100, 250)
t.write("Home Theater", False, align="left", font=("Arial", 20, "bold"))

t.goto(-350, -150)
t.pendown()
t.goto(350, -150)

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(7)

#function to draw the speakers on the sides of the TV
def draw_speaker(x_pos, y_pos):
    t.penup()
    t.goto(x_pos, y_pos)
    t.pendown()
    t.color("black", "purple")
    t.begin_fill()
    t.left(90)
    t.forward(110)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(110)
    t.left(90)
    t.end_fill()
    #speaker circle inside
    t.penup()
    t.goto(x_pos + 20, y_pos + 60)
    t.pendown()

    t.color("black", "yellow")
    t.begin_fill()
    t.circle(12)
    t.end_fill()

t.penup()
t.goto(-180, 0)
t.pendown()
t.pensize(8)
#Bwrown colour from wood sample picture
t.color("#693303")

#cabinet frams
t.forward(360)
t.right(90)

t.forward(150)
t.right(90)
t.forward(360)
t.right(90)
t.forward(150)
t.right(90)

#shelf
t.penup()
t.goto(-180, -75)
t.pendown()
t.forward(360)

t.pensize(2)
#speaker box

t.penup()
t.goto(-140, -75)
t.pendown()
t.color("black", "darkgrey")
t.begin_fill()
t.left(90)
t.forward(55)
t.right(90)
t.forward(110)
t.right(90)
t.forward(55)
t.left(90)
t.end_fill()

#buttons
t.penup()
t.goto(-130, -45)
t.pendown()
t.color("black", "lime")
t.begin_fill()
t.circle(4)
t.end_fill()

t.penup()
t.goto(-115, -45)
t.pendown()
t.color("black", "red")
t.begin_fill()
t.circle(4)
t.end_fill()

#gaming console drawing
t.penup()
t.goto(50, -75)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.left(90)
t.forward(60)
t.right(90)
t.forward(90)
t.right(90)
t.forward(60)
t.left(90)
t.end_fill()

#power lights
t.penup()
t.goto(60, -35)

t.pendown()
t.color("black", "cyan")
t.begin_fill()
t.left(90)
t.forward(5)
t.right(90)
t.forward(35)
t.right(90)
t.forward(5)
t.left(90)
t.end_fill()

#controllers
t.penup()

t.goto(-40, -130)
t.pendown()
t.color("black", "red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(0, -130)
t.pendown()
t.color("black", "lime")
t.begin_fill()
t.circle(10)
t.end_fill()

#tv frame
t.penup()

t.goto(-120, 30)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.left(90)
t.forward(130)
t.right(90)
t.forward(240)
t.right(90)
t.forward(130)
t.left(90)
t.end_fill()

#tv screen
t.penup()
t.goto(-110, 40)
t.pendown()
t.color("black", "cyan")
t.begin_fill()
t.left(90)
t.forward(110)
t.right(90)
t.forward(220)
t.right(90)

t.forward(110)
t.left(90)
t.end_fill()

#tv stand
t.penup()
t.goto(-20, 0)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.left(90)
t.forward(30)


t.right(90)
t.forward(40)
t.right(90)
t.forward(30)
t.left(90)
t.end_fill()

#calling speaker drawing function.
draw_speaker(-170, 0) 

draw_speaker(130, 0) 
turtle.mainloop()