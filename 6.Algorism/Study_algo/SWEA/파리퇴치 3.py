for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    # +
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # x
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    maxV = 0
    for i in range(n):
        for j in range(n): # i,j는 중심 인덱스라고 생각
            dij = 0 # +의 합
            drc = 0 # x
            for s in range(1, m): # 스프레이의 범위내에서
                for k in range(4): # 델타 + 돌아야함
                    ni, nj = i + di[k]*s, j + dj[k]*s  # +
                    nr, nc = i + dr[k]*s, j + dc[k]*s  # x
                    if 0 <= ni < n and 0 <= nj < n:
                        dij += lst[ni][nj] #범위 더하기
                    if 0 <= nr < n and 0 <= nc < n:
                        drc += lst[nr][nc]  # 범위 더하기
            dij += lst[i][j]  # 일단 중심 인덱스 더하고
            drc += lst[i][j]
            if maxV < dij:
                maxV = dij
            elif maxV < drc:
                maxV = drc
    print(f'#{tc} {maxV}')
