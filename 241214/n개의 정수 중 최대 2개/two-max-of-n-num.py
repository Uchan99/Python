n = int(input())

arr = list(map(int, input().split()))
inx = -1
max_val = arr[0]
for i in range(n):
    if max_val <= arr[i]:
        max_val = arr[i]
        idx = i

val = arr[0]
arr[0] = arr[idx]
arr[idx] = val

max_val = arr[1]
for i in range(1, n):
    if max_val <= arr[i]:
        max_val = arr[i]
        idx = i
val = arr[1]
arr[1] = arr[idx]
arr[idx] = val

print(f"{arr[0]} {arr[1]}")

    

    



