arr = []

for _ in range(10):
    arr.append(input())
word = input()
earr = []
for i in range(10):
    if arr[i][-1] == word:
        earr.append(arr[i])

if len(earr) == 0:
    print('None')
else:
    for i in range(len(earr)):
        print(earr[i])