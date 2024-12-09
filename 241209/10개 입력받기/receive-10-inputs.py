arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break
print(sum(arr), end=' ')
print(round(sum(arr)/len(arr), 1))