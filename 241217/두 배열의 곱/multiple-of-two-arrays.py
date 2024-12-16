arr1 = [
    list(map(int, input().split()))
    for _ in range(3)
]
a = input()
arr2 = [
    list(map(int, input().split()))
    for _ in range(3)
] 

arr = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr[i][j] = arr1[i][j] * arr2[i][j]

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()
