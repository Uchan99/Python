n = int(input())
arr = []
for i in range(n):
    input_ = input()
    arr.append(input_)

sum_val = 0
cnt = 0

for i in range(n):
    sum_val += len(arr[i])
    if arr[i][0] == 'a':
        cnt += 1

print(f"{sum_val} {cnt}")