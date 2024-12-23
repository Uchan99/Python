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

if len(arr) >= 10:
    print(len(arr)+1)
elif len(arr) >= 100:
    print(len(arr)+2)
elif len(arr) >= 1000:
    print(len(arr)+3)
else:
    print(len(arr))
    
for elem in arr:
    print(elem, end='')
        

