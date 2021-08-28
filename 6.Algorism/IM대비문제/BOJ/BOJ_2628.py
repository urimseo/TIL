'''
종이자르기
'''
# 종이에서 자른 범위를 비교하면서 가장 큰 수를 찾는것
# 여기서 가장 큰 수가 나오면 가장 긴 가로/세로 길이임.
def maxlen(lst, maxV):
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] > maxV:
            maxV = lst[i + 1] - lst[i]
    return maxV


v, h = map(int, input().split())
n = int(input())
v_cut = [0]  # 가로 길이 처음
h_cut = [0]
for i in range(n):
    ver, hor = map(int, input().split())
    if ver == 0:
        h_cut.append(hor)
    else:
        v_cut.append(hor)

h_cut.append(h)  # 가로길이 끝
v_cut.append(v)  # 세로 길이 끝
v_cut.sort()  # 자른 위치를 정렬해서 잘린 순서대로
h_cut.sort()

mh = maxlen(h_cut, 0) # 가장 긴 가로길이와 세로길이를 구해주기.
mv = maxlen(v_cut, 0)
print(mv * mh)
