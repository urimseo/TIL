'''
# lst.sort(key= lambda i:i[1]) # 두번째 인자 기준 sort 하고 싶을때 사용하는 방법
'''

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()
maxp = [0, 0]

for i in range(n):
    if lst[i][1] >= maxp[1]: # 가장 큰기둥에서 뒤에있는걸 기준점으로 정하기
        maxp = lst[i]

small = []
big = [maxp]
for i in lst:
    if i[0] <= maxp[0]:
        small.append(i)
    else:
        big.append(i)
pillar = [lst[0]]
a = pillar[0][1]

for i in range(1, len(small)): # 두번째 기둥부터 가장 큰 기둥 까지 검사
    if small[0][1] <= small[i][1] <= maxp[1] and a <= small[i][1]:
        a = small[i][1]
        pillar.append(small[i])

pillar2 = [lst[n-1]]
b = pillar2[0][1]
for p in range(len(big)-1, -1, -1):
    if big[-1][1] < big[p][1] <= maxp[1] and b <= big[p][1]:
        b = big[p][1]
        pillar2.append(big[p])

pillar2.append(maxp)

def arr1(p_lst, res):
    for s in range(len(p_lst)-1):
        w = p_lst[s+1][0] - p_lst[s][0]
        h = p_lst[s][1]
        res += w*h
    return res

def arr2(p_lst2, res2):
    for t in range(len(p_lst2)-1):
        w = p_lst2[t][0] - p_lst2[t+1][0]
        h = p_lst2[t][1]
        res2 += w * h
    return res2

total1 = arr1(pillar, 0)
total2 = arr2(pillar2, 0)
print(total1+total2+maxp[1])
