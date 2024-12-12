n = int(input())

arr = list(map(int, input().split()))

cnt = [0] * 10

for elem in arr:
    cnt[elem] += 1

for elem in cnt[1:]:
    print(elem)