def add_score():
    global grade
    apple = input('請輸入科目:')
    yee=int(input("成績:"))
    grade[apple] = yee

def remove_score():
    pass

def out_score():
    pass

grade = {}
while True:
    for k, v in grade.items():
        print(f'{k}={v}')

    print('1. 新增科目')
    print('2. 刪除某個科目的成績')
    print('3. 滾')
    applebananaorange = input('請輸入功能')
    if applebananaorange == "1":
        add_score()

    elif applebananaorange == "2":
        apple = input('刪除某個科目的成績:')
        if apple in grade:
            grade.pop(apple)
        print('已經取消了')

    elif applebananaorange == "3":
        print(f"總平均為:{sum(grade.values())/len(grade)}")
        break
    else:
        print('滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾滾')
