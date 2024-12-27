input_str = input()
n = len(input_str )
ans = input_str[0] + 'a' + input_str[2:n - 2] + 'a' + input_str[n-1:]

print(ans)