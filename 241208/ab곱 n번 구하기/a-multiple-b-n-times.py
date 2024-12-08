n = int(input())
src = 1
for i in range(n):
    src = 1
    a, b = map(int,input().split())
    for j in range(a, b+1):
        src *= j
    print(src)