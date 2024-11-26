arr = []
for i in range(10):
    arr.append(int(input()))
cnt = 0
for i in range(10):
    if arr[i] % 2 == 1:
        cnt += 1

print(cnt)
