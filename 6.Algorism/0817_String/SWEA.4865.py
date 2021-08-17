'''
1. str1에서 str2를 순회하는데
2. 각 숫자마다 돌면서, dictionary?
- counting 정렬...?

c[0] * len(str1)
for j in str2:
for i in str1:
    c[i]


'''
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    # 문자열 key로 가지는 딕셔너리
    c = {}
    for j in str1:
        c[j] = 0
    # 키값과 같으면 value에 +1
    for i in str2:
        if i in c.keys():
            c[i] += 1

    # value 중에 가장 큰 것 찾기
    for v in c.values():
        if maxv < v:
            maxv = v
    print(f'#{tc} {maxv}')



# print(c[0])
# for i in range(s1):
#     for k in str1:
#         for j in str2:
#             if k == j:
#                 c[i] += 1
# print(c)