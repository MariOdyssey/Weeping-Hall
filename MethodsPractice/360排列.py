import sys
n = int(input())
b = input().split()
min = sys.maxsize
for i in range(0, n):
    num = 0
    for j in range(0, n):
        num += abs(int(b[j]) - j - 1)
    if num < min:
        min = num
    b.append(b[0])
    b.pop(0)
print(min)