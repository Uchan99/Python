arr = ["apple", "banana", "grape", "blueberry", "orange"]

given_input = input()

ok_arr = []
cnt = 0

for i in range(len(arr)):
    if arr[i][2] == given_input or arr[i][3] == given_input:
        cnt += 1
        ok_arr.append(arr[i])

for i in range(len(ok_arr)):
    print(ok_arr[i])
print(cnt)

