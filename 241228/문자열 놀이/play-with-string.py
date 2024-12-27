s, q = input().split()

q = int(q)

for _ in range(q):
    t, a, b = input().split()
    t = int(t)
    if t == 1:
        s = list(s)
        a = int(a)
        b = int(b)
        tmp = s[a-1]
        s[a-1] = s[b-1]
        s[b-1] = tmp
        s = ''.join(s)
        print(s)
    elif t == 2:
        s  = list(s)
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        s = ''.join(s)
        print(s)

    
