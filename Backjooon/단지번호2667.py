import sys
input = sys.stdin.readline

N = int(input())

maps = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]

result, each = [], 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if maps[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(N):
    for i in range(N):
        if maps[j][i] == 1 and chk[j][i] == False:
            each = 0
            chk[j][i] = True
            dfs(j, i)
            result.append(each)

result.sort()
print(len(result))
for elem in result:
    print(elem)