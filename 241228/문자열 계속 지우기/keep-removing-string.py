A = input()
B = input()
b = len(B)

exist = True
while exist == True:
    if A == b:
        A = []
    exist = False
    for i in range(len(A) - b):
        if A[i:i+b] == B:
            A = A[:i] + A[i+b:]
            exist = True
            break
        
print(A)