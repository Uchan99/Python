input_str = input()

arr = list(input_str)
a1 = arr[0]
a2 = arr[1]
for i in range(len(arr)):
    if arr[i] == a1:
        arr[i] = a2
    elif arr[i]  == a2:
        arr[i] = a1

arr = ''.join(arr)
print(arr)