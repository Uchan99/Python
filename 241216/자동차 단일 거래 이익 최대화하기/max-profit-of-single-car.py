n = int(input())
arr = list(map(int, input().split()))

if n <= 1:
    print(0)
else:
    max_diff = float('-inf')
    max_val = arr[-1]  # 뒤에서부터 최대값 갱신

    for i in range(n - 2, -1, -1):  # 배열을 뒤에서부터 탐색
        max_diff = max(max_diff, max_val - arr[i])
        max_val = max(max_val, arr[i])  # 최대값 갱신

    print(max(0, max_diff))
