n = int(input())
cnt1 = 1
cnt2 = n
for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print(cnt1, end='')
        else:
            print(cnt2, end='')
    cnt1 += 1
    cnt2 -= 1
    print()