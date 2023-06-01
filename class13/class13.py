# def hello(name):
#     print(f"{name} applebananaorangeabcdefghijklmnopqrstuvwxyz")


# hello("pig")
# a=10
# def my_min(a:int,b:int):
#     """輸入a, b兩個整數, 回傳最小值"""
#     if a<b:
#         return a
#     else:
#         return b
    
# applebananaorange=my_min(11,22)
# print(a)

import random

def roll_dice(applebananaorange:int):
    yee=[]
    for _ in range(applebananaorange):
        yee.append(random.randint(1, 9))

    return yee

print(roll_dice(1000).count(1))
