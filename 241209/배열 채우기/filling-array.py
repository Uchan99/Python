arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
    
for elem in arr[::-1]:
    print(elem, end=' ')
    