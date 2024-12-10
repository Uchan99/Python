n = int(input())

arr = list(map(int, input().split()))
arr = arr[::-1]
for elem in arr:
    if elem % 2 == 0:
        print(elem, end=' ')