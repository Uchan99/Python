n = int(input())

arr = list(map(int, input().split()))
max_arr = []

for i in range(n-1):
    max_arr.append(max(arr[i+1:]) - arr[i])

if max(max_arr) <= 0:
    print(0)
else:
    print(max(max_arr))
