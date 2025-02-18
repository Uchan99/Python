import sys
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d= map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
sw = False

while True:
    if maps[y][x] == 0:
        maps[y][x] = 2
        cnt += 1
    sw = False
    for k in range(1, 5):
        ny = y + dy[d-k]
        nx = x + dx[d-k]
        if 0 <= ny < N and 0 <= nx < M:
            if maps[ny][nx] == 0:
                d = (d-k+4)%4
                y = ny
                x = nx
                sw = True
                break
    if sw == False:
        ny = y - dy[d]
        nx = x - dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if maps[ny][nx] != 1:
                y = ny
                x = nx
            else:
                break   
                
print(cnt)


    

