t = int(input())
for tc in range(1, t+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    maxw = 0
    maxh = 0
    for i in range(N):
        cntw = 0
        cnth = 0
        for j in range(N):
            if lst[i][j] == 1: #한번의 행에서 가로길이
                cntw += 1
            if lst[j][i] == 1:
                cnth += 1 # 한번의 행에서 세로길이
        if maxw < cntw:
            maxw = cntw
        if maxh < cnth:
            maxh = cnth

    print(f'#{tc} {maxh*maxw}')