arr = [
    list(map(int, input().split()))
    for _ in range(2)
]


for i in range(2):
    sum_hor = 0
    for j in range(4):
        sum_hor += arr[i][j]
    print(sum_hor/4, end=' ')
print()

for i in range(4):
    sum_ver = 0
    for j in range(2):
        sum_ver += arr[j][i]
    print(sum_ver/2, end=' ')
print()

sum_val = 0
for i in range(2):
    for j in range(4):
        sum_val += arr[i][j]

print(sum_val/8)
        