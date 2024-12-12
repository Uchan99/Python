n = int(input())
arr = []
cnt = 0
cnto = 1

while cnt < 2:
    arr.append(n * cnto)
    cnto += 1
    current = arr.pop()
    print(current, end=' ')
    if current % 5 == 0:
        cnt += 1
    
