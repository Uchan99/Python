arr = []
sum_val = 0
cnt = 0
for i in range(10):
    arr.append(int(input()))
    if arr[i] >= 0 and arr[i] <= 200:
        sum_val += arr[i]
        cnt += 1

print(f"{sum_val} {round(sum_val/cnt, 1)}")

