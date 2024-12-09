arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        arr = arr[::-1]
    
for elem in arr:
    print(elem, end=' ')
    