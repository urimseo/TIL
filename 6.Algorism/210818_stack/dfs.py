'''
7 8
1 2
1 3


# V, E = map(int, input().split())
# ad = [[0]*(V+1) for _ in range(V+1)]
#
# for _ in range(E): # 엣지의 갯수만큼
#     n1, n2 = map(int, input().split())
#     ad[n1][n2] = 1 # 단방향의 경우
#     ad[n2][n1] = 1 # 방향이 없는경우
'''


def dfs(s, V):
    visited = [0] * (V + 1)
    stack = []
    i = s  # 현재 방문한 정점 i
    visited[i] = 1
    print(visited)

    print(node[i]) # 처음 시작 정점도 같이 출력해줘야함
    while i != 0:  # True
        for w in range(1, V + 1):
            if adj[i][w] == 1 and visited[w] == 0:  # 1 은 인접이라는 말, 0은 방문하지 않았다는 뜻
                stack.append(i)  # 현재 i 방문 경로 저장
                i = w  # 새 방문지 이동
                visited[w] = 1  # 새 방문지 방문했다가 표시하기
                print(node[i])  # 실제 방문한 방문지 출력
                break
        else:
            if stack:  # stack에 있으면 (과거에 방문 했던 곳이면)
                i = stack.pop()
            else:  # 없으면 탐색 종료..?
                i = 0


# 인접행렬
#          A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0],  # A
       [0, 1, 0, 0, 1, 1, 0, 0],  # B
       [0, 1, 1, 0, 0, 1, 0, 0],  # C
       [0, 0, 1, 0, 0, 0, 1, 0],  # D
       [0, 0, 1, 1, 0, 0, 1, 0],  # E
       [0, 0, 0, 0, 1, 1, 0, 1],  # F
       [0, 0, 0, 0, 0, 0, 1, 0]]  # G
node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
dfs(1, 7)  # 1번부터 돌리고 총 7개가 있다.
