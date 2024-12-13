n = int(input())

arr = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            arr[i] = -1
            arr[j] = -1

if max(arr) == -1:
    print(-1)
else:
    print(max(arr))