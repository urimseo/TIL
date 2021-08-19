'''
    # arr = [list(map(int, input().split())) for _ in range (E)]
그래프경로
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6
'''

T = int(input())
for tc in range(1, T+1):
    vertex, edge = map(int, input().split())
    adj = [[0]*(vertex+1) for _ in range(vertex+1)]  # 0으로만 되어있는 행렬

    for _ in range(edge):  # 경로를 0-> 1로 바꿔줌
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1  # 단방향

    start, end = map(int, input().split())  # 시작, 끝 경로    # 시작정점의 배열 ...
    visited = [0] * (vertex+1)  # 인덱스 123 그대로 사용할거라 +1 (0 사용 안함)
    visited[start] = 1 # 시작점은 1로 표시해놓기
    stack = []
    ans = 0 # 경로 있으면 1, 없으면 0
    while ans != 1: # 도착지에 갔으면 탐색 종료
        for w in range(1, vertex+1): # w는 다음에 방문할 장소
            if adj[start][w] == 1 and visited[w] == 0:
                stack.append(start)   # 현재 지점 표시
                start = w  # 다음으로 이동
                visited[w] = 1  # 이동한 지점 1표시
                if visited[end] == 1:  # 도착지점이 1이면 경로가 있다는 뜻
                    ans = 1
                    break
                else:
                    ans = 0
                break
        else: # 되돌아가자
            if stack: # stack 있으면 되돌아 갈 수 있다.
                start = stack.pop() # 마지막 이동지점 제거하고 이전으로 돌아가기
    print(f'#{tc} {ans}')













