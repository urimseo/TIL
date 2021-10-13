'''
마지막 정점 번호, 간선 수
(P.16 - 아래쪽 그림 )
6 8
0 1 0 2 0 5 0 6 4 3 5 3 5 4 6 4
0-1 0-2 0-5 0-6 4-3 5-3 5-4 6-4
'''

V, E = map(int, input().split())
edge = list(map(int, input().split()))

# 인접행렬로 저장하는 경우
adjM = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):  # 총 8개 엣지, 출발+도착 = 16개
    n1, n2 = edge[2*i], edge[2*i+1]  # n1, n2 연결되어있음
    adjM[n1][n2] = 1                 # 방향성 그래프이면 여기서 끝
    adjM[n2][n1] = 1                 # 무향 그래프인 경우
print(adjM)

# 인접 리스트로 저장하는 경우
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adjL[n1].append(n2)
print(adjL) 
