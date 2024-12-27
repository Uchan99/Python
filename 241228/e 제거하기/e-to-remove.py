a = input()
a = list(a)
n = len(a)
idx = -1
for i in range(n):
    if a[i] == 'e':
        idx = i
        break
a = a[:idx] + a[idx+1:]
a = ''.join(a)
print(a)