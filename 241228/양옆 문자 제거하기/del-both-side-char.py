s = input()
n = len(s)
s = s[:1] + s[2:n-2] + s[n-1]
print(s)