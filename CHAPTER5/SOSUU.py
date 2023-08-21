def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

# ユーザーから入力を受け取る
try:
    num = int(input("素数判定を行う数を入力してください: "))
    if is_prime(num):
        print(f"{num} は素数です")
    else:
        print(f"{num} は素数ではありません")
except ValueError:
    print("正しい数値を入力してください")


