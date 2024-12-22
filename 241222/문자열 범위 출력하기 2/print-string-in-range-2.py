arr = input()
n = int(input())
len_arr = len(arr)

if len_arr > n:
    # 문자열의 마지막 n개를 역순으로 출력
    for i in range(len_arr - 1, len_arr - 1 - n, -1):
        print(arr[i], end='')
else:
    # 문자열이 n보다 짧을 때, 전체 문자열만 출력
    for i in range(len_arr):
        print(arr[i], end='')

