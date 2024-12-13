n, q = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        print(arr[que[1]-1])
    elif que[0] == 2:
        idx = -1
        for j in range(n):
            if arr[j] == que[1]:
                idx = j + 1
                print(idx)
                break
        if idx == -1:
            print(0)
    elif que[0] == 3:
        for j in range(que[1], que[2] + 1):
            print(arr[j-1], end=' ')
        print()