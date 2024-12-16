n = int(input())

arr = list(map(int, input().split()))

min_val = float('inf')

for i in range(n-1):
    for j in range(i+1, n):
        diff = abs(arr[j] - arr[i])
        if diff < min_val:
            min_val = diff
print(min_val)
        