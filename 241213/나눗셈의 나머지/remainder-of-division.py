a, b = map(int, input().split())

cnt = [0] * 10

while a > 1:
    cnt[a % b] += 1
    a //= b

sum_val = 0
sum_val += sum(val ** 2 for val in cnt)

print(sum_val)