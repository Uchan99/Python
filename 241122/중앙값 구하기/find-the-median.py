a, b, c = map(int, input().split())

if a > b:
    if a > c:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b > c:
        if c > a:
            print(c)
        else:
            print(a)
    else:
        print(b) 