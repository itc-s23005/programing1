def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 入力を受け取る
N = int(input())
numbers = []
for _ in range(N):
    d = int(input())
    numbers.append(d)

# バブルソートで降順に並び替える
bubble_sort(numbers)

# 結果をスペース区切りで出力
print(' '.join(map(str, numbers)))

