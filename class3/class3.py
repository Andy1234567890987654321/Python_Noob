# print("請輸入生日:", end='')
# eval() 自動偵測字串的內容，如果是數字會轉成整數或小數，如果可以計算會自動計算完之後在存回變數，如果有任何文字就會錯誤
# a= int(input("請輸入生日:"))
# # print(a+a)
# # print(a*100)
# print(type(a))
# a = input("輸入自己的年齡：")
# # print("你的年齡是")
# # print(a)

# print("你的年齡是", end='')
# print(a, end='')
# print("歲!")

# print("你的年齡是" + a + "歲!")
# print("你的年齡是{}歲!".format(a))
# print("你的年齡是%s歲!" % a)
# print(f"你的年齡是{a}歲!")
pi=3.14
r=int(input("請輸入半徑："))
Area=pi*r**2
print(Area)