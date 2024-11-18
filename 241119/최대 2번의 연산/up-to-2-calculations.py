a = int(input())

if a % 2 == 0:
    a = int(a/2)
if a % 2 == 1:
    a = a + 1
    a =int(a/2)

print(a)