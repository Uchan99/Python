n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
num = 1
for k in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                arr[i][j] = num
                num += 1
                break

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()
        
            

