a1, t1 = input().split()
a2, t2 = input().split()
a3, t3 = input().split()

t1 = int(t1)
t2 = int(t2)
t3 = int(t3)

if a1 == 'Y' and t1 >= 37:
    if (a2 =='Y' and t2 >= 37) or (a3 =='Y' and t3 >= 37):
        print('E')
    else:
        print('N')
else:
    if (a2 =='Y' and t2 >= 37) and (a3 =='Y' and t3 >= 37):
        print('E')
    else:
        print('N')