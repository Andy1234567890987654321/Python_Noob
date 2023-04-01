# == is same
# != is different
# >= is more than and =
# <= is less than and =
# > is more than
# < is less than

############################################################################
# 1 ()
# 2 **次方ˋ直
# 3 正負數
# 4 乘法 * 小數除法 / 整數除法 // 取餘數 ％
# 5 加法 減法
# 6 == != >= <= > <
# 7 not and or
############################################################################
# password = input("請輸入密碼")
# if password == "1234":
#     print("歡迎光臨person a")
# elif password == "5678":
#     print("歡迎光臨person b")
# else:
#     print("密碼錯誤")
############################################################################
# password = input("請輸入密碼")
# if password == "1234" or password == "5678" or password == "12345678" or password == "3.1415926535897932384626433849502884197169399375":
#     print("歡迎光臨")
# else:
#     print("密碼錯誤")
############################################################################
try:
    score = int(input("請輸入分數:"))
except:
    print("請輸入數字分數!")
else:
    if score >= 90:
        print("A")
    elif score >= 80 and score <= 89:
        print("B")
    elif score >= 70 and score <= 79:
        print("C")
    elif score >= 60 and score <= 69:
        print("D")
    else:
        print("E")
