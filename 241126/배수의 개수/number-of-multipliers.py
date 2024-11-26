arr = []
for i in range(10):
    arr.append(int(input()))

cnt3 = 0
cnt5 = 0
for i in range(10):
    if arr[i] % 3 == 0:
        cnt3 += 1
    if arr[i] % 5 == 0:
        cnt5 += 1

print(cnt3, end= ' ')
print(cnt5)