s = input()
cc = len(s)
cnt = 0

while cc - cnt > 1:
    a = int(input())
    if a > cc - cnt:
        s = s[:-1]
        print(s)
        cnt += 1
    else:
        s = s[:a] + s[a+1:]
        print(s)
        cnt += 1