'''
타일로봇
w = p[3] - p[1]
h = p[2] - p[0]
'''
# for tc in range(1, int(input())+1):
#     n = int(input())
#     lst = [list(map(int, input().split())) for _ in range(n)]
#     tile = []
#     for p in lst:
#         for i in range(p[2] - p[0]+1):
#             for j in range(p[3] - p[1]+1):
#                 x = p[0] + i
#                 y = p[1] + j
#                 if [x, y] not in tile:
#                     tile.append([x,y])
#     print('#{} {}'.format(tc, len(tile)))

for tc in range(1, int(input())+1):
    arr = [[0]*10 for _ in range(10)]
    n = int(input())
    for i in range(n):
        h1, w1, h2, w2 = map(int, input().split())
        for a in range(h1, h2+1):
            for b in range(w1, w2+1):
                arr[a][b] = 1

    res = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] ==1:
                res += 1
    print('#{} {}'.format(tc, res))