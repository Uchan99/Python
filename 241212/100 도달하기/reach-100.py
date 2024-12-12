n = int(input())

arr = [0, 0]

arr[0], arr[1] = 1, n

i = 2
while True:
    arr.append(arr[i-1] + arr[i-2])
    if arr[i] > 100:
        break
    i += 1
for elem in arr:
    print(elem, end= ' ')
