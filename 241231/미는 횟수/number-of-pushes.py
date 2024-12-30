A = input()
B = input()
cnt = 0
while True:
    cnt += 1
    A = A[-1] + A[:-1]
    if A == B:
        break
    if cnt == len(A):
        cnt = -1
        break

print(cnt)