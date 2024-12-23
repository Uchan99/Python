A = input()

cnt = 1
current = A[0]
arr = []
if len(A) != 1:
    for i in range(1, len(A)):
        if i == len(A) - 1:
            if A[i] == current:
                cnt += 1
                arr.append(current)
                arr.append(cnt)
            else:
                arr.append(current)
                arr.append(cnt)
                current = A[i]
                cnt = 1
                arr.append(current)
                arr.append(cnt)
        else:
            if A[i] == current:
                cnt += 1
            else:
                arr.append(current)
                arr.append(cnt)
                current = A[i]
                cnt = 1
else:
    arr.append(current)
    arr.append(cnt)
ccnt = 0
for i in range(1, len(arr), 2):
    if arr[i] >= 1000:
        ccnt += 3
    elif arr[i] >= 100:
        ccnt += 2
    elif arr[i] >= 10:
        ccnt += 1
 
print(len(arr) + ccnt)

for elem in arr:
    print(elem, end='')
        

