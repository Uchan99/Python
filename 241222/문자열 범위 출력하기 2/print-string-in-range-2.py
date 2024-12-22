arr = input()
n = int(input())
len_arr = len(arr)

if len_arr > n:
    # 문자열의 마지막 n개를 역순으로 출력
    for i in range(len_arr - 1, len_arr - 1 - n, -1):
        print(arr[i], end='')
else:
    # 문자열을 반복해서 n개의 문자 출력
    for i in range(n):
        print(arr[i % len_arr], end='')
