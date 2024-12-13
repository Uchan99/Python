arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break

score = [0] * 11

for elem in arr:
    score[elem // 10] += 1

for i in range(10, 0, -1):
    print(f"{i * 10} - {score[i]}") 