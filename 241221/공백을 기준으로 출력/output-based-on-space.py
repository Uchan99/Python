a = input()
b = input()

for i in range(len(a)):
    if a[i] == ' ':
        print('', end='')
    else:
        print(a[i], end='')

for i in range(len(b)):
    if b[i] == ' ':
        print('',end='')
    else:
        print(b[i],end='')
