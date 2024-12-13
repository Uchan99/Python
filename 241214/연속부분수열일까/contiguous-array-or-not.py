n1, n2 = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

idx = -1
cnt = 0
for i in range(len(arr_a)):
    if arr_a[i] == arr_b[0]:
        idx = i
        break
arr_a = arr_a[i:i+n2]

if arr_a == arr_b:
    print('Yes')
else:
    print('No')

    

