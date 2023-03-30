try:
    num = int(input('請輸入一個數字:'))
    total = num+1
    print(total)
except ValueError:
    print('你未輸入數字')
except:
    print('發生錯誤')
else:
    print('success')
finally:
    print('程式結束')
