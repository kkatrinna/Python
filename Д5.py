import turtle
'''
turtle.reset()
turtle.up()
turtle.goto(-50, 50)
turtle.down()
turtle.begin_fill()
turtle.goto(50, 50)
turtle.goto(50, -50)
turtle.goto(-50, -50)
turtle.goto(-50, 50)
turtle.end_fill()

turtle.up()
turtle.goto(-90, 100)
turtle.down()
turtle.forward(100)
turtle.right(90)
turtle.forward(-50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(-50)

turtle.up()
turtle.goto(-200, 0)
turtle.down()
turtle.goto(-100, 0)
turtle.goto(-100, 60)
turtle.goto(-200, 0)

turtle.up()
turtle.goto(200, 0)
turtle.down()
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()

turtle.done()
'''


#3
'''
turtle.reset()
turtle.width(2)

turtle.up()
turtle.begin_fill()
turtle.color('black', 'blue')
turtle.goto(-200, 150)
turtle.down()
turtle.goto(50, 110)
turtle.goto(-10, 85)
turtle.goto(-200,150)
turtle.end_fill()

turtle.up()
turtle.goto(-10, 85)
turtle.down()
turtle.goto(-20, 20)

turtle.begin_fill()
turtle.color('black', 'blue')
turtle.goto(-35, 50)
turtle.goto(-200, 150)
turtle.up()
turtle.goto(-20, 20)
turtle.down()
turtle.goto(-60, 37)
turtle.end_fill()

turtle.up()
turtle.goto(-35, 50)
turtle.down()
turtle.begin_fill()
turtle.color('black', 'blue')
turtle.goto(-90, 20)
turtle.goto(-200, 150)
turtle.end_fill()

turtle.up()
turtle.begin_fill()
turtle.color('black', 'blue')
turtle.goto(-20, 20)
turtle.down()
turtle.goto(-60, 37)
turtle.end_fill()



turtle.up()
turtle.goto(45, 100)
turtle.down()
turtle.goto(120, 90)
turtle.up()
turtle.goto(20, 84)
turtle.down()
turtle.goto(140, 75)
turtle.up()
turtle.goto(0, 50)
turtle.down()
turtle.goto(50, 15)
turtle.up()
turtle.goto(-60, 25)
turtle.down()
turtle.goto(70, -10)

turtle.begin_fill()
turtle.up()
turtle.goto(140, 180)
turtle.down()
turtle.color('yellow', 'yellow')
turtle.circle(30)
turtle.end_fill()
'''

#4
'''
turtle.reset()
turtle.width(5)


turtle.begin_fill()
turtle.color('#606060', '#FFB266')
turtle.up()
turtle.goto(5, 49)
turtle.down()
turtle.right(270)
turtle.circle(20, 80)
turtle.forward(25)
turtle.circle(50, 100)
turtle.forward(120)
turtle.circle(10, 90)
turtle.forward(20)
turtle.circle(10, 90)
turtle.forward(30)
turtle.right(90)
turtle.circle(60, 35)
turtle.up()
turtle.goto(-40, -68)
turtle.down()
turtle.right(115)
turtle.forward(25)
turtle.circle(10, 80)
turtle.forward(15)
turtle.circle(10, 80)
turtle.forward(40)
turtle.circle(250, 12)

turtle.up()
turtle.goto(-95, 28)
turtle.down()
turtle.left(95)
turtle.forward(20)
turtle.circle(10, 83)
turtle.forward(70)
turtle.circle(10, 90)
turtle.forward(15)
turtle.end_fill()

turtle.begin_fill()
turtle.color('orange')
turtle.up()
turtle.goto(6, -23)
turtle.down()
turtle.left(90)
turtle.forward(50)
turtle.circle(40, 100)
turtle.forward(25)
turtle.circle(20, 80)
turtle.forward(60)
turtle.circle(20, 80)
turtle.forward(25)
turtle.circle(45, 70)
turtle.end_fill()

turtle.up()
turtle.goto(10, 0)
turtle.down()
turtle.right(60)
turtle.begin_fill()
turtle.color('#003366', '#3399FF')
turtle.circle(20, 90)
turtle.forward(5)
turtle.circle(20, 90)
turtle.forward(40)
turtle.circle(20, 90)
turtle.forward(5)
turtle.circle(20, 90)
turtle.forward(40)
turtle.circle(20, 90)
turtle.end_fill()

turtle.begin_fill()
turtle.color('#66B2FF')
turtle.up()
turtle.goto(-40, 30)
turtle.down()
turtle.left(180)
turtle.circle(10, 90)
turtle.forward(45)
turtle.circle(10, 90)
turtle.circle(10, 90)
turtle.forward(45)
turtle.circle(10, 90)
turtle.end_fill()

turtle.begin_fill()
turtle.color('white')
turtle.up()
turtle.goto(20, 35)
turtle.down()
turtle.right(10)
turtle.forward(2)

turtle.end_fill()
'''

import turtle as t
screen = turtle. Screen ()
screen.setup(500, 600, startx=0, starty=100)
s = turtle. Screen ()
s.bgcolor("black")
t. color("green")
a = 0
b = 0
t.speed (0)
t. up()
t.goto(0,200)
t. down ()
while(True):
    t. forward (a)
    t.right(b)
    a+=3
    b+=1
    if b == 210:
        break
    t.hideturtle()

turtle.done()


'''
import turtle as t


t.color('red', 'yellow')
t.speed(6)
t.fd(-150)
t.begin_fill()
s = t.Screen()

for i in range(90) :
    t.forward(300)
    t.left(170)
t.end_fill()
'''





































