n = int(input())
asc = n + 64

for i in range(n):
    for j in range(n):
        print(chr(asc), end="")
        asc += 1
    print()