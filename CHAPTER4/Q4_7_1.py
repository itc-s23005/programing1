def make_addfunc():
    print('足し算する関数を作成')
    def add(x, y):
        print('{} + {} = {}'.format(x, y, x + y))
        return x + y
    return add
