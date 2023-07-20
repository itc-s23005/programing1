def number_to_day(num):
    # 任意の整数が与えられたら今日、昨日、それ以外を判定しして返す#

    昨日(num=-1)
    今日(num=0)
    明日(num=1)
    今日より1日を超えて離れた日(num=over)

   if num == 0:
       day = "今日"
   elif num == 1:
       day = "明日"
    elif num == -1:
        day = "昨日"
    else:
        day = "今日より１日を超えて離れた日"

    return day
