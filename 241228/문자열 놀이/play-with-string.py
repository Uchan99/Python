s, q = input().split()

q = int(q)

for _ in range(q):
    t, a, b = input().split()
    t = int(t)
    if t == 1:
        a = int(a)
        b = int(b)
        s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
        print(s)
    elif t == 2:
        s  = list(s)
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        s = ''.join(s)
        print(s)

    
