n = int(input())
lst = list(map(int, input().split()))
maxV = 0
minV = lst[0]

for i in lst:
    if maxV < i:
        maxV = i
    if minV > i:
        minV = i
print(maxV-minV)