'''
l = []
while True:
    applebananaorange = input('新增東西:')
    if applebananaorange == "end":
        break
    else:
        l.append(applebananaorange)
        print(l)

while True:
    applebananaorange = input('移除東西:')
    if applebananaorange == "end":
        break
    else:
        while applebananaorange in l:
            l.remove(applebananaorange)
        print(l)

while True:
    applebananaorange = input('計算東西數量:')
    if applebananaorange == "end":
        break
    else:
        print(l.count(applebananaorange))
'''
m = ['可口可樂', '月亮蝦餅', '黃咖哩炒蝦']
yee = []
while True:
    print(yee)
    print('1. 新增餐點')
    print('2. 移除餐點')
    print('3. 提交菜單')
    applebananaorange = input('請輸入功能')
    if applebananaorange == "1":
        for orange in range(len(m)):
            print(f'{orange+1}. {m[orange]}')

        apple = int(input('請輸入餐點:'))
        if apple > len(m):
            print('滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾')
        else:
            yee.append(m[apple-1])

    elif applebananaorange == "2":
        apple = input('請輸入移除餐點:')
        while apple in yee:
            yee.remove(apple)

        print('已經取消了')

    elif applebananaorange == "3":
        print(f"可口可樂x{yee.count('可口可樂')}")
        print(f"月亮蝦餅x{yee.count('月亮蝦餅')}")
        print(f"黃咖哩炒蝦x{yee.count('黃咖哩炒蝦')}")
        break
    else:
        print('滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾')
