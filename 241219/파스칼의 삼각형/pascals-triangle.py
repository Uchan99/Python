n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]


for i in range(n):
    for j in range(i+1):
        if j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for row in arr:
    for elem in row:
        if elem != 0:
            print(elem, end=' ')
    print()