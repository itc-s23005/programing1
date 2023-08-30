with open("my_math2.py", "w") as f:
    f.writellines('''def my_pow(x, y):
    return x ** y
if __ name__ == "__main__":
    x, y, exp = 2, 5, 32
    ans = my_pow({},{}) →  {}, exp: {} ---- ".format(x, y, ans,
exp), end="")
    if ans == exp:
        print("Test OK")
    else:
        print("Test Fail")\n''')
