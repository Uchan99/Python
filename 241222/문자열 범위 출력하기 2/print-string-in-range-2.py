arr = input()
n = int(input())

if len(arr) > n:
    for i in range(len(arr)- 1,len(arr) - 1 - n, -1):
        print(arr[i], end='')
else:
    for i in range(n):
        print(arr[i], end='')