data = input()
word, char = data.split()
position = word.find(char)


if position != -1:
    print(position)
else:
    print("No")
