n = int(input())

arr = list(map(int, input().split()))

tot = ""

for elem in arr:
    tot += str(elem)

for i in range(len(tot)):
    if i != 0 and i % 5 == 4:
        print(tot[i])
    else:
        print(tot[i], end='')