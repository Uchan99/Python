n = int(input())

arr = list(map(int, input().split()))
cnt = 0
min_val = min(arr)

for elem in arr:
    if min_val == elem:
        cnt += 1
print(f"{min_val} {cnt}")
