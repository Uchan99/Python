n = int(input())

for i in range(n):
    for k in range(i):
        print(' ', end=' ')
    for j in range(2 * n - 2 * i - 1):
        print('*', end=' ')
    print()
for i in range(1, n):
    for k in range(n -1 -i):
        print(' ', end =' ')
    for j in range(2 * i + 1):
        print('*', end =' ')
    print()