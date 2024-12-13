n1, n2 = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

idx = -1
cnt = 0
for i in range(len(arr_a)):
    if arr_a[i] == arr_b[0]:
        idx = i
if idx == -1:
    print('No')
else:
    for i in range(len(arr_b)):
        if arr_a[i + idx] != arr_b[i]:
            cnt += 1
            break
if cnt == 0:
    print('Yes')
else:
    print('No')


    

