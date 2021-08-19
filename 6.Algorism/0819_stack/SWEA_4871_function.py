

def dfs(s, g, V):
    stack = []
    visited = [0] * (V+1)
    n = s # 현재 방문한 정점
    visited[n] = 1
    while n > 0: # 방문한 접점이 있으면
        # 현재 정점에 인접하고 방문하지 않은 정점 w찾기

        for w in range(1, V+1):
            if adj[n][w] == 1 and visited[w] == 0: # w가 n에 인접하고 미방문이면
                stack.append[n] # 현재 위치를 경로로 저장
                n = w
                visited[n] = 1
                # 방문한 정점에서 할 일 -> 목적지(g)에 도착했는지 확인 .
                if n == g: # 현재 위치가 도착지면
                    return 1
                break  # 목적지가 아니면, 현재 n을 기준으로 다시 w찾기
        else:
            if stack:
                n = stack.pop()
            else:
                n = 0  # while문 빠져나가기 위함. return 0 여기서 해도 상관 없다.

    return 0






T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
    s, g = map(int, input().split())  # 마지막 정점 (정점개수), 간선개수

print()