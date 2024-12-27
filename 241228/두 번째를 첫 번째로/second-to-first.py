s = input()

s = list(s)
an = s[1]

for i in range(len(s)):
    if s[i] == an:
        s[i] = s[0]

s = ''.join(s)
print(s)