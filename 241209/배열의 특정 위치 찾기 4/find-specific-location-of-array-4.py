arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break

cnt = 0
sum_val = 0

for elem in arr:
    if elem % 2 == 0:
        sum_val += elem
        cnt += 1

print(f"{cnt} {sum_val}")