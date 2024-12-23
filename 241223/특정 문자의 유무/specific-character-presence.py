existee = 'No'
existab = 'No'

input_str = input()

for i in range(len(input_str)-1):
    if input_str[i] == 'e' and input_str[i+1] == 'e':
        existee = 'Yes'
    if input_str[i] == 'a' and input_str[i+1] == 'b':
        existab = 'Yes'

print(f"{existee} {existab}")

    
