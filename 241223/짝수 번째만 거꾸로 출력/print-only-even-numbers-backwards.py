a = input()
arr = []
for i in range(1, len(a), 2):
    arr.append(a[i])

for elem in arr[::-1]:
    print(elem, end='')