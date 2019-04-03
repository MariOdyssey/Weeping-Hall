m = input().split(' ')[1]
b = input().split(' ')
c =[]
for i in b:
    c.append(int(i))
for i in range(0, int(m)):
    t, x = input().split(' ')
    if t == '0':
        temp = c[0:int(x)]
        temp.sort()
        c[0:int(x)] = temp
    else:
        temp = c[0:int(x)]
        temp.sort()
        temp.reverse()
        c[0:int(x)] = temp
print(c)