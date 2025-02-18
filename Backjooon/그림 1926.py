from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt, maxv = 0, 0

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(y, x):
    rs = 1
    q = deque([(y, x)])

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny, nx = ey + dy[k], ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    rs += 1
                    q.append((ny,nx))
                
    return rs
                
for j in range(n):
    for i in range(m):
        if maps[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)