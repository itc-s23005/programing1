def gen_prime(x=2):
    '''素数を返すジェネレータ関数(1)愚直な方法'''
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
            else:
                yield x
            x += 1                
                            
