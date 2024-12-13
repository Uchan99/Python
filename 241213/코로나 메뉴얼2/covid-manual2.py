a = ['a'] * 3
b = [0] * 3
cnt = [0] * 4
for i in range(3):
    arr = list(input().split())
    a[i] = arr[0]
    b[i] = int(arr[1])
    if a[i] == 'Y':
        if b[i] >= 37:
            cnt[0] += 1
        else:
            cnt[2] += 1
    else:
        if b[i] >= 37:
            cnt[1] += 1
        else:
            cnt[3] += 1

if cnt[0] >= 2:
    for elem in cnt:
        print(elem, end= ' ')
    print('E')
else:
    for elem in cnt:
        print(elem, end=' ')