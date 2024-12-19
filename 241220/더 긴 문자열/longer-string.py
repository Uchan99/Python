arr1, arr2 = input().split()


if len(arr1) > len(arr2):
    print(arr1, end =' ')
    print(len(arr1))
elif len(arr1) == len(arr2):
    print('same')
else:
    print(arr2, end=' ')
    print(len(arr2))