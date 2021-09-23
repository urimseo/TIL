'''
# lst.sort(key= lambda i:i[1]) # 두번째 인자 기준 sort 하고 싶을때 사용하는 방법
'''

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()
print(lst)
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
pillar = [lst[0]] # 첫번째는 그냥 넣어
a = pillar[0][1]
#  lst[i][0] <= maxp[0] and
# 기둥 순서가 가장 큰거보다 작거나 같고, 기둥 높이가 처음 기둥과 크거나 같고, 가장 큰 기둥보다 작거나 같으면 ..
for i in range(1, len(small)): # 두번째 기둥부터 가장 큰 기둥 까지 검사
    if small[0][1] <= small[i][1] <= maxp[1] and a <= small[i][1]: # lst[i][0]은 처음 기둥이니 포함됨
        a = small[i][1]  # 6 5 6 3 4
        pillar.append(small[i])  # 6 3 4  6 3 4 # 각각의 오른쪽의 높은 애가 뭔지 알아야함..

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


# for s in range(len(pillar)):  #작은거 검사..
#     if pillar[s][0] < maxp[0]: # 기준기둥보다 작은 경우 앞기둥 ~ 뒷기둥 전까지 면적 더하기
#         w = pillar[s+1][0] - pillar[s][0]
#         h = pillar[s][1]
#         res += w*h
#     elif pillar[s][0] == maxp[0]:  # 가장 큰 기둥은 일단 더하기
#         res += maxp[1]
#     else: # 그 뒤는 더 작은 기둥 or 기준기둥과 같은 높이의 기둥만 나오게 되어있음
#         # 뒤의 기둥에서 앞에꺼랑 뺴야함..
#         w = pillar[s][0] - pillar[s-1][0]   # 뒤의 기둥위치 - 현재 기둥 위치 (앞의 기둥은 포함 안하고 뒤의 기둥만 포함 )
#         h = pillar[s][1]  # 뒤의 기둥 높이 (더 낮음)
#         res += w*h
# print(res)

#
#










# while flag != 0:
#     i = 0  # 인덱스
#     flag = 0
#     while (i + 1) < len(lst)-1:  # 인덱스 범위가 넘어가지 않으면
#         i += 1 # 인덱스 번호 증가                                         # while 문 끝날때까지 flag 0이면 더이상 뺄 게 없다는 뜻임.
#         if lst[i - 1][1] > lst[i][1] and lst[i + 1][1] > lst[i][1]:
#             lst.pop(i)
#             flag += 1
# res = 0
# for s in range(len(lst)):
#     if s == len(lst)-1:  # 마지막일 경우
#         res += lst[s][1]
#
#     elif lst[s+1][1] < lst[s][1]:  # 뒤의 기둥이 더 낮을 경우
#         w = lst[s+1][0] - lst[s][0] - 1   # 뒤의 기둥위치 - 현재 기둥 위치 -1 (뒤의 기둥, 앞의 기둥 포함 안하는 너비)
#         h = lst[s+1][1]  # 뒤의 기둥 높이 (더 낮음)
#         res += (w*h) + lst[s][1]  # 앞의 기둥높이 + 뒤의 면적
#     else:
#         w = lst[s+1][0] - lst[s][0]
#         h = lst[s][1]
#         res += w*h
# print(res)


    # 뒤에가 더 작을 경우  경우
    # 가로  = > lst[i+1][0] - lst[i][0]
    # 세로 => lst[i][1]

    # 만약 마지막 인덱스일 경우에는
    # 자기 자신 더하기  += lst[i][1]



