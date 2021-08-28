'''
# 7 : 노드수 , 8 : 엣지수
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 6 7 3 7
'''


# 인접 리스트로
def bfs3(s, V):  # s는 시작점
    q = [0] * V  # 큐 생성
    front, rear = -1, -1
    visited = [0] * (V + 1)  # visited 생성
    rear += 1
    q[rear] = s
    visited[s] = 1  # 시작점 visited

    while front != rear: # 큐가 비어잇지 않으면
        front += 1
        t = q[front]
        print(t) # 현재의 노드
        for i in range(1, V+1):  # t에 인접하고 미방문인 모든 i에 대해
            if adj[t][i] == 1 and visited[i] == 0:
                rear += 1
                q[rear] = i
                visited[i] = visited[t] + 1


V, E = map(int, input().split())
edge = list(map(int, input().split()))
# 인접행렬 만들기
adj = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 행렬
adjlst = [[] for _ in range(V + 1)]  # 인접 리스트

for i in range(E):
    n1, n2 = edge[2 * i], edge[2 * i + 1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1  # 방향이 없는 그래프에선 양쪽 연결

    adjlst[n1].append(n2)
    adjlst[n2].append(n1)
# print(adjlst)

bfs3(1, V)
