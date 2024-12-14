n = int(input())

arr = list(map(int, input().split()))

arr_vals = []

for i in range(n-1):
    arr_val = max(arr[i+1:]) - arr[i]
    if arr_val > 0:
        arr_vals.append(arr_val)

print(max(arr_vals))
