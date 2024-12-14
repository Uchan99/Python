n = int(input())

arr = list(map(int, input().split()))

idxs = []
bound = n
idx = -1
while bound > 0:
    max_val = arr[0]
    idx = 0
    for i in range(bound):
        if max_val < arr[i]:
            max_val = arr[i]
            idx = i
    idxs.append(idx + 1)
    bound = idx

for elem in idxs:
    print(elem, end=' ')
