
for tc in range(1, 11):
    t = int(input())
    n = 100
    lst = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0
    # 대각선
    left = 0
    right = 0
    for i in range(100):
        resw = 0
        resh = 0
        #대각선 검사는 i에서만 하면됨
        left += lst[i][n - 1 - i]
        right += lst[i][i]
        for j in range(100):
            resw += lst[i][j]
            resh += lst[j][i]
        #대소비교 행, 열 여기서 한번 해주고,
        if resw > maxV:
            maxV = resw
        if resh > maxV:
            maxV = resh
    # 대각선도 대소비교 해줘야함
    if maxV < right:
        maxV = right
    if maxV < left:
        maxV = left

    print(f'#{t} {maxV}')