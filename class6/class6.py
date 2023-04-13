# import turtle
# applebananaorange = 100
# applebananaorangegrape = 90
# applebananaorangegrapepen = 100000000
# applebananaorangegrapepencil = 10000000000
# turtle.speed(10)
# turtle.forward(applebananaorange)
# turtle.backward(applebananaorangegrape)
# turtle.right(applebananaorangegrapepen)
# turtle.left(applebananaorangegrapepencil)
# turtle.done()

import time
import turtle
turtle.speed(10)

for loop in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.done()


turtle.speed(0)
turtle.forward(100)
turtle.backward(100)
time.sleep(1)  # 休息1秒
turtle.right(6)
time.sleep(1)  # 休息1秒
turtle.clear()
turtle.forward(100)
turtle.backward(100)
time.sleep(1)  # 休息1秒
turtle.right(6)
time.sleep(1)  # 休息1秒
turtle.clear()
turtle.done()
