'''
請製作一個指令(使用def)
使用者可以輸入x,y座標
turtle會移動到該座標畫一棵樹
turtle.goto(x, y)
'''
import turtle
import random

big_apple = 100
def appleorangebanana(x, y):
    global big_apple
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    r=random.randint(0,255)/255
    g=random.randint(0,255)/255
    b=random.randint(0,255)/255

    turtle.fillcolor((r, g, b))
    turtle.begin_fill()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()

    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)

    r=random.randint(0,255)/255
    g=random.randint(0,255)/255
    b=random.randint(0,255)/255

    turtle.fillcolor((r, g, b))
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(70)
    turtle.left(120)
    turtle.forward(70)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()


turtle.speed(0)
c = int(input("tree number:"))
for loop in range(c):
    appleorangebanana(random.randint(-200,200), random.randint(-200,200))

turtle.done()
