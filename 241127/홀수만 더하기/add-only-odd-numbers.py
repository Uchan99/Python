n = int(input())

arr = []
sum_val = 0

for i in range(n):
    arr.append(int(input()))
    if arr[i] % 2 == 1 and arr[i] % 3 ==0:
        sum_val += arr[i]

print(sum_val)

