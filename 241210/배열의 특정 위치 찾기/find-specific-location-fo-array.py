arr = list(map(int, input().split()))
sum_val = 0
for i in range(1, 11, 2):
    sum_val += arr[i]
avg_val = 0
for i in range(2, 11, 3):
    avg_val += arr[i]
avg_val /= 3

print(sum_val, end=' ')
print(round(avg_val, 1))