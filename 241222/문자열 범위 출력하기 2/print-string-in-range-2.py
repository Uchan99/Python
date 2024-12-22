arr = input()
n = int(input())
len_arr = len(arr)
if len_arr > n:
    for i in range(len_arr- 1,len_arr - 1 - n, -1):
        print(arr[i], end='')
else:
    for i in range(n):
        print(arr[i], end='')