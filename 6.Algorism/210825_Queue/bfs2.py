'''
# 7 : 노드수 , 8 : 엣지수
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 6 7 3 7
'''
# 인접 리스트로
def bfs2(s,V):
    ####초기화######
    q = []                # 큐 생성
    visited =[0] * (V+1)  # visited 생성
    q.append(s)           # 시작점 enq
    visited[s] = 1        # 시작점 visited 표시

    while q:# 큐가 비어있지 않으면 (처리할 정점이 남아 있으면)
        t = q.pop(0) # 디큐(꺼내서)해서 t에 저장
        print(t)# t에 대한 처리
        for i in adjlst[t]:   # 인접인 애 꺼내서
            if visited[i] == 0: # 방문 유무만 확인
                q.append(i)                  # enqueue(i)
                visited[i] = visited[t] + 1  # i visited로 표시



V, E = map(int, input().split())
edge = list(map(int, input().split()))
#인접행렬 만들기
adj = [[0]* (V+1) for _ in range(V+1)] # 인접 행렬
adjlst = [[] for _ in range(V+1)]  # 인접 리스트
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1  # 방향이 없는 그래프에선 양쪽 연결

    adjlst[n1].append(n2)
    adjlst[n2].append(n1)
# print(adjlst)

bfs2(1, V)