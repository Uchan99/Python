s = input()

while len(s) != 1:
    a = int(input())
    if a > len(s):
        s = s[:-1]
        print(s)
    else:
        s = s[:a] + s[a+1:]
        print(s)