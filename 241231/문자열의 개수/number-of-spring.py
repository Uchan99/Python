arr = []
cnt = 0

while True:
    inp = input()
    if inp == '0':
        break
    else:
        cnt += 1
        if cnt % 2 == 1:
            arr.append(inp)

print(cnt)
for elem in arr:
    print(elem)