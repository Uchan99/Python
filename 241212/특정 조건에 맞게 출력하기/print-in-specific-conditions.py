arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break

for elem in arr:
    if elem % 2 == 0:
        print(elem // 2, end =' ')
    else:
        print(elem + 3, end =' ')