import random

secret_number = random.randint(1, 100)
guess_count = 0

print("欢迎来到猜数字游戏！")
print("我想了一个1-100之间的数字，你来猜！")

while True:
    try:
        guess = int(input("请输入你猜的数字："))
    except ValueError:
        print(" 请输入一个有效的整数！")
        continue

    guess_count += 1

    if guess == secret_number:
        print(f"恭喜你猜对了！答案就是{secret_number}")
        print(f"你一共猜了{guess_count}次")
        break
    elif guess < secret_number:
        print("太小了！再往大猜~")
    else:
        print("太大了！再往小猜~")