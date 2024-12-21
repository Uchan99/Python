given_input = input()

a = input()
cnt = 0
for i in range(len(given_input)):
    if given_input[i] == a:
        cnt += 1

print(cnt)
