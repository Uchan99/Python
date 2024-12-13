# ***
n = int(input())
arr = list(map(int, input().split()))

count = [0] * 1001

for num in arr:
    count[num] += 1

unique_numbers = [i for i in range(1, 1001) if count[i] == 1]

if not unique_numbers:
    print(-1)
else:
    print(max(unique_numbers)) 
