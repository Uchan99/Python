arr = list(map(int, input().split()))

min_ = []
max_ = []

for elem in arr:
    if elem < 500:
        min_.append(elem)
    else:
        max_.append(elem)

print(f"{max(min_)} {min(max_)}")