n = int(input())
ns = []
sum_val = 0
cnt = 0

for i in range(n):
    ns.append(int(input()))
    sum_val += ns[i]
    cnt += 1

print(f"{sum_val} {round(sum_val/cnt, 1)}")
