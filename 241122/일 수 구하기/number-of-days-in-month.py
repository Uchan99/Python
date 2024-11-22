n = int(input())

if n < 8:
    if n % 2 == 1:
        print('31')
    elif n == 2:
        print('28')
    else:
        print('30')
else:
    if n % 2 == 0:
        print('31')
    else:
        print('30')