"""
請使用turtle模組以及for印出以下圖形
t0_turtle_stamp.jpg
提示：
turtle.home()是讓烏龜回到原點的指令
"""

"""
五邊形星星
"""
import turtle
turtle.penup()
turtle.stamp()
turtle.right(0)
for loop in range(8):
    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.right(45)
turtle.done()
