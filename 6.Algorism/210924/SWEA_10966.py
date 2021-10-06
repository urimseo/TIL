'''
믈놀이를 가자
BFS -> 출발점이 여러곳이 가능 하다.
q에 각각 출발점을 넣고, 출발점을 하나씩 빼...
--------------
| w1, w2, L, L, L ...
------------


- 물에서 땅을 찾자

- 물이 2개 이상일 때
-> 시작지점에 물을 모두 담고 시작.W1, W2 L1, L2...L3등..
Q 에 담을때 -> 좌표, 좌표/거리
'''
from _collections import deque
# 상하좌우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())  # N : 세로크기, M: 가로크기
#     arr = [input() for _ in range(N)]
#     dist = [[987654321] * M for _ in range(N)]  # 방문체크 & 거리 체크
#
#     # Q = deque()
#
#     # Q 직접 구현하기 (선형큐)
#     Q = [0] * (N*M)
#     front = -1 # 뭘 의미하니
#     rear = -1
#
#     # 시작점인 물을 몽땅 담아두기 위해서
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] =='W':
#                 # Q.append((i, j))
#                 rear += 1
#                 Q[rear] = (i, j)
#                 dist[i][j] = 0
#
#     # while Q:
#     while front != rear:
#         # r, c = Q.popleft()  # 맨 앞에 있는거 꺼내기
#         front += 1
#         r, c = Q[front]
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
#             if arr[nr][nc] == 'L' and dist[nr][nc] == 987654321:  # 땅이거나, dist 의 좌표가 같으면 -> 방문을 하지 않은 곳이면
#                 dist[nr][nc] = dist[r][c] + 1  # 기존에 있는 값보다 한칸 더가
#                 # Q.append((nr, nc))
#                 rear += 1
#                 Q[rear] = (nr, nc)
#     ans = 0
#
#     for i in dist:
#         for j in i:
#             ans += j
#
#     print(f'#{tc} {ans}')


# 웹액스 풀이
def bfs(N, M):
    front = -1
    rear = -1

    q = [0] * (N*M) # 큐생성 -> 모든 칸이 큐에 들어갈 수 있음. 만약 모르겠으면 그냥 크게 만들기
    visited = [[0]*M for _ in range(N)]# visited 생성
    # 시작점('W' -> 물인 모든 칸 ) 인큐, 방문표시 -> front, rear로 만들기
    for i in range(N):
        for j in range(M):
            if arr[i][j] =='W':
                rear += 1
                q[rear] = (i, j)
                visited[i][j] = 1

    while front != rear:     #큐가 비어있지 않으면 반복..
        front += 1# deque 디큐
        i, j = q[front]
        # 모든 칸을 탐색하므로, i, j 칸에 대해 처리할 것은 없다.
        # 인접칸 탐색 시작
        for di, dj in [[0, 1], [1, 0],[0, -1], [-1, 0]]: # 인접하고, 방문하지 않은 칸이면
            ni, nj = i + di, j + dj
            if 0<= ni < N and 0<nj<= M and visited[ni][nj] ==0: # 인접이면
                # 인큐하고 방문표시해아함. bfs를 기본적으로 이해해야함.. 근데 난 못해찌
                rear += 1 # 인큐
                q[rear] = (ni, nj)
                visited[ni][nj] = visited[i][j] + 1 # 방문표시

    s = 0
    for i in range(N):
        for j in range(M):
            s += visited[i][j]
    return s - N*M

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)] # 문자열로 저장
    # arr = [list(input()) for _ in range(N)]  # 리스트로 글자 잘라서 저장 -> 수정을 해야하는 경우에는 리스트로 저장 하는게 좋음

    print(bfs(N, M))

