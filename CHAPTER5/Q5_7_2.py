下記の会員場号、会員の性別、氏名、年齢、都道府県の表をもとに、データを格納する辞書を生成するプログラムを作成してください。
まず、表を入れ子のリストデータとして生成し、会員場号を辞書のキー、それ以外のレコードをリスト関数として辞書の値とし、辞書変数に格納するとします。

'0001' Male Yamada Tarou 25 Tokyo

'0002' Male Satou Tskashi 27 Kanagawa

'0003' Female Tanaka Yuko 25 Saitama

'0004' Male Suzuki Ichirou 35 Hokkaido

# 表データの作成
data = [
    ['0001' , 'Male' , 'Yamada' , 'Tarou' , 25 , 'Tokyo']
    ['0002' , 'Male' , 'Satou' , 'Takeshi' , 27 , 'Kanagawa']
    ['0003' , 'Female' , 'Tanaka' , 'Yuko' , 25 , 'Saitama']
    ['0004' , 'Male' , 'Suzuki' , 'Ichirouu' , 35 , 'Hokkaidou']
    ]
data
