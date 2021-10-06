
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    wlst = []
    hlst = []
    for i in range(n):
        resw = 0
        resh = 0
        for j in range(n):
            resw += lst[i][j]
            resh += lst[j][i]
        wlst.append(resw)
        hlst.append(resh)

    maxV = 0
    total = 0
    for i in range(len(wlst)):
        for j in range(len(hlst)):
            total = wlst[i] + hlst[j] - lst[i][j]
            if maxV < total:
                maxV = total

    print(f'#{tc} {maxV}')