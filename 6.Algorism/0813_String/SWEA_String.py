# '''
# 1.
# '''
    for i in range(10):
        TC = int(input())
        pattern = input()
        text = input()
        Plen = len(pattern)
        Tlen = len(text)

        p = 0 # pattern 인덱스   3
        t = 0 # text의 인덱스    10
        cnt = 0 # 찾은 인덱스 수
        res = 0 # 찾은 패턴 수
        while t <= Tlen-Plen+1 and p < Plen:
            if text[t] == pattern[p]:
                t += 1
                p += 1
                cnt += 1
                if cnt == Plen:
                    res += 1
                    p = 0
                    cnt = 0
                elif t != Tlen and text[t] == pattern[0] and cnt > 0:
                    p = 0
                    cnt = 0
            else:
                t += 1
                p, cnt = 0, 0
        print(f'#{TC} {res}')



# for T in range(10):
#     TC = int(input())
#     pattern = list(input())
#     text = list(input())
#     cnt = 0
#
#     for i in range(len(text) - len(pattern) + 1):
#         for j in range(len(pattern)):
#             # 불일치
#             if pattern[j] != text[i + j]:
#                 break  # i+1
#         else:
#             cnt += 1
#
#     print(f'#{TC} {cnt}')