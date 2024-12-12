arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break

cnt = [0] * 10

for elem in arr:
    cnt[elem // 10] += 1

for i in range(1, 10):
    print(f"{i} - {cnt[i]}")