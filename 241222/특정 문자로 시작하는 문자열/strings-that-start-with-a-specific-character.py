n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
word = input()
cnt = 0
earr = []
for i in range(n):
    if arr[i][0] == word:
        earr.append(arr[i])
        cnt += 1

avg = 0
for i in range(len(earr)):
    avg += len(earr[i])

avg = avg/len(earr)
print(f"{cnt} {avg:.2f}")


