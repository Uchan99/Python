a = input()
b = input()

idx = -1

for i in range(len(a) - len(b) + 1):  # 범위 수정
    if a[i:i+len(b)] == b:  # 부분 문자열 비교
        idx = i
        break

print(idx)
