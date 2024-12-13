word = ['L', 'E', 'B', 'R', 'O', 'S']
moon = input()
idx = -1

for i, char in enumerate(word):
    if char == moon:
        idx = i

if idx == -1:
    print('None')
else:
    print(idx)