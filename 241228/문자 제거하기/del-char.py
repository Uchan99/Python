s = input()

while len(s) > 1:
    a = int(input())
    if a > len(s):
        s = s[:len(s)-1]
        print(s)
    else:
        s = list(s)
        s.pop(a)
        s = ''.join(s)
        print(s)