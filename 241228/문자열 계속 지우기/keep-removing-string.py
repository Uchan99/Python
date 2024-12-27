A = input()
B = input()
b = len(B)

exist = True

while exist:
    exist = False
    index = A.find(B)  # B가 A에 존재하는지 확인
    
    if index != -1:  # B가 A에 존재하면
        A = A[:index] + A[index + b:]  # B를 제거
        exist = True  # 다시 탐색 진행

print(A)
