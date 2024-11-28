sum_val = 0
cnt = 0
while True:
    age = int(input())
    if age // 10 != 2:
        break
    else:
        sum_val += age
        cnt += 1

print(format(round(sum_val/cnt, 2), ".2f"))
