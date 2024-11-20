s = int(input())
a = int(input())

if s == 0:
    if a < 19:
        print('BOY')
    else:
        print('MAN')
else:
    if a < 19:
        print('GIRL')
    else:
        print('WOMAN')