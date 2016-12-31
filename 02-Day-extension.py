import random
secret = random.randint(1,10)
print('------------demo 2------------')
temp = input('不妨猜一下小甲鱼现在心里想的是哪个数字:')
guess = int(temp)
count = 0
while (guess != secret) and (count < 3):   
    count = count + 1
    print(count)
    if guess == 8:
        print("卧槽,你是小甲鱼心里的蛔虫吗?")
        print('哼,猜中了也没有奖励!')
    else:
        if guess > 8:
            print("大了大了")
        else:
            print('小了小了')
    if count < 3:
        temp = input("哎呀,猜错了,请重新输入吧:")
        guess = int(temp)
if guess == secret:
    print("卧槽,你是小甲鱼心里的蛔虫吗?")
else:
    print("尝试多次失败!")
print("游戏结束,不玩啦^_^");
