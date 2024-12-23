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
                arr.append(str(cnt))
            else:
                arr.append(current)
                arr.append(str(cnt))
                current = A[i]
                cnt = 1
                arr.append(current)
                arr.append(str(cnt))
        else:
            if A[i] == current:
                cnt += 1
            else:
                arr.append(current)
                # cnt를 문자열로 변환 후, 각 자릿수를 분리해서 추가
                for digit in str(cnt):
                    arr.append(digit)
                current = A[i]
                cnt = 1
else:
    arr.append(current)
    arr.append(cnt)

print(len(arr))
for elem in arr:
    print(elem, end='')
        

