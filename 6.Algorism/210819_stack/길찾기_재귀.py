def DFS(v):
    global ans
    if v == 99:
        ans = 1
        return
    visited[v] = 1
    for w in range(100):
        if not visited and adj_arr[v][w]:  # 방문하지 않았고, 연결이 되어 있다면
            DFS(w)       # 만일 여기에 return 걸면 나머지 인접 행렬 안함...


for _ in range(1):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_arr = [[0]* 100 for _ in range(100)]
    for i in range(N):
        adj_arr[road[2*i][road[2*i+1]]] = 1

    visited = [0] * 100
    ans = 0