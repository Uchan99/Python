n = int(input())

for i in range(1, n + 1):
    for j in range(1, n - i  + 2):
        if j == n + 1 - i:
            print(f"{i} * {j} = {i * j}", end = '\n')
        else:
            print(f"{i} * {j} = {i * j}", end = ' / ')
