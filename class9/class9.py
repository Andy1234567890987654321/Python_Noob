'''
從一顯示到六，三以後的不顯示
'''

# i = 1
# while i < 600000
#     if i == 599999:
#         break
#     print(i)
#     i += 1


# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

while True:
    applebananaorange = input('請給我錢!')
    if applebananaorange == "1":
        print('apple juice')
    elif applebananaorange == "2":
        print("orange juice")
    elif applebananaorange == "3":
        print('grape juice')
    elif "4" in applebananaorange:
        break
    else:
        print('三倍金錢')
