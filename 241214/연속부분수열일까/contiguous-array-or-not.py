n1, n2 = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

idx = -1
cnt = 0
for i in range(len(arr_a)):
    arr_a_idx =[]
    if arr_a[i] == arr_b[0]:
        idx = i
        arr_a_idx = arr_a[i:i+n2]
    if arr_a_idx == arr_b:
        print('Yes')
        cnt += 1
        break

if cnt == 0:
    print('No')


print(arr_a_idx)
print(arr_b)

    

