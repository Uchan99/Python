arr = []
cnt = 0

for i in range(5):
    arr.append(int(input()))
    if arr[i] % 2 == 0:
        cnt += 1

print(cnt)