n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

for i in range(n):
    if arr[i] % 2 == 1 and arr[i] % 3 == 0:
        print(arr[i])