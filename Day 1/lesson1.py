from turtle import *

shape("turtle")
#we want to paint a house

#step 1: we draw the walls
width(7)
color("gray")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

#endofsquare

#drawimg a door
forward(70)
color("brown")
begin_fill()
left(90)

forward(100)
right(90)

forward(60)
right(90)

forward(100)
end_fill()

#endofdoor

#drawing a roof

penup()
goto(200,200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

#endoftheroof

#drawing windows

penup()
goto(20,120)
pendown()

color("yellow")
begin_fill()
right(150)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

penup()
goto(180,120)
pendown()

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
end_fill()

#endofthewindows


exitonclick()




