n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 or i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print(0, end = ' ')
    elif 30 <= i < 40:
        print(0, end = ' ')
    elif 60 <= i < 70:
        print(0, end = ' ')
    elif 90 <= i < 100:
        print(0, end = ' ')
    else:
        print(i, end=' ')