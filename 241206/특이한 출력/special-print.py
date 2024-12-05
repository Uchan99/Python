n = int(input())
cnt = 3
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == cnt:
            print(f"({i}, {j})", end='\n')
            cnt -= 1
        else:
            print(f"({i}, {j})", end=' ')