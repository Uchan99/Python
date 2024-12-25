a = input()
b = input()

idx = -1

find = False
for i in range(len(a) - len(b)):
    if find == True:
        break
    else:
        if a[i] == b[0]:
            idx = i
            for j in range(1, len(b)):
                if j == len(b) - 1:
                    find = True
                    break
                if a[i + j] == b[j]:
                    continue
                else:
                    idx = -1
                    break

print(idx)
    
    
            
            

        