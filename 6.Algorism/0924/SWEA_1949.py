''''
등산로 조성
인접칸으로 이동
- 이웃칸, 더 낮고(or 깎는 횟수가 남아있고 깎아서 더 낮아진다면 ok) 등산로에 포함되지 않은 칸

'''

def f(i, j, N, K, c, s):  # i, j 칸이 등산로에 포함, 깎는 횟수: c, 이전까지의 길이 s
    global maxV       # 최대 등산로 길이
    if maxV < s + 1:
        maxV = s+1    # 최대 등산로 길이 갱신
    v[i][j] = 1  # 현재 등산로에 포함된 칸
    # 주변 칸 탐색
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
            if arr[i][j] > arr[ni][nj]:        # 인접칸이 더 낮은 경우
                f(ni, nj, N, K, c, s + 1)   
            elif c == 1 and arr[i][j] > arr[ni][nj] - K:  # 인접칸이 더 높지만, 깎을 수 있고, 깎았을 때 낮아져서 이동 가능한 경우 # 깎고 이동 가능 한 경우
                tmp = arr[ni][nj]  # 깎기 전의 높이 저장
                arr[ni][nj] = arr[i][j] - 1  # 1만 깎는게 좋음! 그래야지 이동 가능한 위치가 더 많아지기 때문
                f(ni, nj, N, K, c-1, s+1) # c는 여기서 0이 됨. s+1로 길이는 한칸 늘어나게 만들기
                arr[ni][nj] = tmp # 원래 길이로 복구

    v[i][j] = 0  # i, j 칸을 이전의 다른 경로에서 사용할 수 있도록 방문 표시를 풀어주기

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]  # 등산로에 표시된 곳 찾기
    # 최대 높이 찾기
    h = 0
    for i in range(N):
        for j in range(N):
            if h < arr[i][j]:
                h = arr[i][j]

    # 최대 높이인 곳에서 등산로를 만들어보기
    maxV = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == h:
                f(i, j, N, K, 1, 0) # i, j 에서부터 등산로 만들어보기, 깎을 수 있는 횟수, 지금까지의 등산로 길이

'''
# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1. 현재 위치를 들고 다니지 않을 때
# r, c 좌표, road: 지금까지 조성된 등산로의 길이, skill: 공사  유무
def work (r, c, road, skill):
    global ans
    if road > ans: ans = road

    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
            # a. 현 위치보다 낮은 곳으로 이동할 때
            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road+1, skill)
            # b. 현 위치보다 높거나 같은 곳으로 이동할 때 ->
            elif skill and mountain[nr][nc] -K < mountain[r][c]:
                tmp = mountain[nr][nr] # 기록 해놓기 깎는 위치
                mountain[nr][nc] = mountain[r][c] -1
                work(nr, nc, road+1, 0) # 스킬 사용했으니 0 임
                mountain[nr][nc] = tmp

# 2. 현재 위치를 들고 다닐 경우
def work2(r, c, h, road, skill):
    global ans
    if road > ans: ans = road

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc>= N or visited[nr][nc]: continue # 범위를 벗어나거나 이미 방문한 경우는 할 필요가 없으니 continue

        if h > mountain[nr][nc]:
            work2(nr, nc, mountain[nr][nc], road+1, skill)
        elif skill and h > mountain[nr][nc]-K:
            work2(nr, nc, mountain[r][c]-1, road+1, 0) # 현재 위치에서 -1 한 것이 다음 이동할 좌표의 높이가 됨..? 뭔 개소리야



for tc in range(1, int(input())+1):
    N, K = map(int, input().split()) # N: 한변의 길이, K: 최대 공사가 가능한 깊이
    # N * N 크기의 2차원 리스트(배열)이 주어진다.
    # mountain = [list(map(int, input().split())) for _ in range(N)]
    # max_h = 0 # 최대 높이
    # for i in range(N):
    #     for j in range(N):
    #         if max_h < mountain[i][j]:
    #             max_h = mountain[i][j]

    # 입력을 받으면서 큰 수를 찾기
    mountain = []
    max_h = 0
    for i in range(N):
        tmp = list(map(int, input().split()))
        # 한 줄 입력을 받고 내부에서 가장 큰 값을 찾자!
        for j in tmp:
            if max_h < j:
                max_h = j
        mountain.append(tmp) # 큰 수를 찾고 tmp를 mountain에 저장해서 등산로를 작성

        visited = [[0]*N for _ in range(N)]
        ans = 0 # 등산로의 길이 -> 최종 출력할 길이. 함수 내부로 끌고 들어가서 최대 길이를 ans로 저장

        for i in range(N):
            for j in range(N):
                if mountain[i][j] == max_h: # 가장 높은 봉우리가 여러개 일 수 있음.
                    # work(i, j, 1,1) # 좌표i, j, 길, skill
                    work2(i, j, max_h, 1, 1) # 좌표, 높이, 길, skill
    print(f'#{tc} {ans}')

'''






















