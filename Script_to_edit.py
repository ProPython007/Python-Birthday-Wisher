
#  CODE BAADME DEKHNA PEHLE RUN KAR !!!

from pygame import mixer
import time
from time import sleep
import turtle
import random
import sys
mixer.init()
mixer.music.load("HBD.mp3")
mixer.music.play(2)
st="""\n\nBefore telling you HBD
I want to tell you something:

We all have that friend
we may not talk to
them everyday, but
they understand us
more than anyone in
the world. U know
they'll always be there
for you in your time of
need when none of
your other friends will.
To that friend I just
wanna say I love u
& thank you for
always being a true
friend..
Best friends remember all the things they did together,
all the mistakes they made all the fun they had
No matter how much their lives may change, their
friendship remains the same. I know that throughout my life
wherever I am, I will always remember so well and cherish
our friendship, as one of the best I have ever known.

So... Happy Birthday Bhai !!!
Bht cute sa b********a ha tu asehi rhna jasa ha...
Party baadme dena abhi tu cake dekh !\n"""
for i in st:
    print(i, end='')
    sys.stdout.flush()
    sleep(0.1)
mixer.music.stop()
time.sleep(.5)
mixer.music.load("HBD2.mp3")
mixer.music.play()
bg = turtle.Screen()
bg.bgcolor("black")
turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)
turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)
turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)
turtle.penup()
turtle.goto(-100,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()
for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)
    time.sleep(1)
time.sleep(1)
turtle.penup()
turtle.goto(-150, 50)
turtle.color("white")
turtle.pendown()
turtle.write("HAPPY BIRTHDAY BHAI !","24pt bold")
time.sleep(10)
turtle.write("   Rap kaisa ha bol ?  Sunn !","24pt bold")
turtle.color("black")
time.sleep(85)

input()

# PARTY TOH DENA HI PAREGA TUJHE !!!
