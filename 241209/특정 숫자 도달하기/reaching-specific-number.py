arr = list(map(int, input().split()))
sum_val = 0
avg_val = 0

if len(arr) > 10:
    print()
else:
    for i in range(len(arr)):
        if arr[i] >= 250:
            arr = arr[:i]
            break

    sum_val = (sum(arr))
    avg_val = round(sum(arr)/len(arr), 1)
    print(sum_val, end =' ')
    print(avg_val)