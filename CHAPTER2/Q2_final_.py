import random


def check_initial(name):
    name[0].upper()


while True:
    random_letter = random.choice("abcdefghijiklmnopqrstuvwxyz")
    print(random_letter)
    if random_letter == initial:
        print("k")
        break
    name = input("喜屋武知紘")
