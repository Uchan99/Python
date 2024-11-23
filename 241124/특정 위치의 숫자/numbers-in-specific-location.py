arr = list(map(int, input().split()))
sum = 0
for i in range(len(arr)):
    if i == 2 or i == 4 or i == 9:
        sum += arr[i]

print(sum)