t = int(input())
for tc in range(1, t+1):

    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    k = 4
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    maxV = 0
    for i in range(n):
        for j in range(m):
            res = 0
            for p in range(k):
                for a in range(1, lst[i][j] + 1):  # 2
                    ni = i + (di[p] * a)
                    nj = j + (dj[p] * a)
                    if 0<= ni<= n-1 and 0<= nj <= m-1:
                        res += lst[ni][nj]
            res += lst[i][j]
            if res > maxV:
                maxV = res
    print(f'#{tc} {maxV}')
