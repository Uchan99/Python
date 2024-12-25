str_input = input()
cnte = 0
cntb = 0
for i in range(len(str_input) - 1):
    if str_input[i] == 'e':
        if str_input[i+1] == 'e':
            cnte += 1
        elif str_input[i+1] == 'b':
            cntb += 1

print(f"{cnte} {cntb}")