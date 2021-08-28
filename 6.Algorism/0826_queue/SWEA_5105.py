'''
미로의 거리
최소 칸수 찾기
못찾겠다 꽤꼬리
'''
def maze(i, j, n, cnt): # i, j -시작 인덱스, n - 미로크기, c-지나온 경로의 개수,
    global minV
    if lst[i][j] == 2:#도착했으면
        if minV > cnt-1:
            minV = cnt-1
        return
    else:
        lst[i][j] = 1 # 방문표시
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni , nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] != 1:
                maze(ni, nj, n , cnt+1)
        lst[i][j] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]
    minV = N*N # 최소 경로 최대로 초기화
    a,b = 0, 0 # 미로 시작점
    for r in range(N):
        for c in range(N):
            if lst[r][c] == 3:
                a, b = r, c

    maze(a, b, N, 0)

    if minV == N*N:  # 경로가 없는 경우
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {minV}')
