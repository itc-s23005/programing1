0から20までの整数を要素としてとしてもつ集合Aと、0以上20以下の偶数を要素として持つ集合Bを作成し、集合Aと集合Bの演算によって0以上20以下の偶数ではない(奇数である)数を要素とする集合Cを生成してみましょう

A = {x for x in range(21)}
print(A)
B = {x for x in range(21) if x % 2 == 0}
print(B)
C == A - B
print(C)