arr = input()
n = int(input())

if len(arr) > n:
    arr = arr[::-1]
    for i in range(n):
        print(arr[i], end='')
else:
    for elem in arr:
        print(elem,end='')