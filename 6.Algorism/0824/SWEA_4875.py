'''
미로
'''
def f2(i, j, N):
    # if maze[i][j] == 3:  # 출구에 도착한 경우
    #     return 1

        maze[i][j] = 2  # i, j 방문표시 (진입한 칸을 벽으로 변경함)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:  # and visited[ni][nj] = 0
                if f2(ni, nj, N):  # 출구를 찾고 리턴하면
                    return 1  # 입구까지 리턴(남겨둔 갈림길을 탐색하지 않음)
            elif 0 <= ni <N and 0 <= nj < N and maze[ni][nj] == 3:
                return 1
        return 0  # 탐색 방향에서 출구를 찾지 못한 경우

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    sti = 0
    stj = 0
    for a in range(n):
        for b in range(n):
            if maze[a][b] == 2:  # 시작점 찾기
                sti = a
                stj = b
    print(f'#{tc} {f2(sti, stj, n)}')