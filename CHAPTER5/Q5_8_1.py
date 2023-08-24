次のプログラムを実行したときの出力結果として、正しいものはどれでしょうか？

country_code = {
    'Icekande': {'code': '354', 'capital': 'Reykjavik'}
    'Irelande': {'code': '353', 'capital': 'Dublin'}
    'Azerbaidijan': {'code': '994', 'capital': 'Baku'}
    }

def getstr_keyval(x):
    if not isinstance(x, dict):
        return x

    my_str = ''
    for key, val in x,items():
        my_str += (' ' + str(key) + ' ' + getstr_keyval(val))
    return my_str

for key1, val1 in country_code,items():
    print(key1), getstr_keybal(val1))

1 順不同
  Icelande code 354 capital Reykjavik Irelande code 353  capital Dublin Azerbaidjan code 994 capital,Baku

2 行順不同
  Icelande (code 354)(capital Reykjavik)
  Irekande (code 353)(capital Dublin)
  Azerbaidjan (code 994)(capital Baku)

3
  Icelande code 354 capital Reykjavik
  Irelande code 353 capital Dublin
  Azerbaidjan code 994 capital Baku

4 順不同、行順不同
  Icelande code 354 capital Reykjavik
  Irelande code 353 capital Dublin
  Azerbaidjan code 994 capital Baku

4  
