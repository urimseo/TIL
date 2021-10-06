'''
길찾기
input이 문제
1 16  -> 16개의 노드


[[0, 1], [0, 2], [1, 4], [1, 3], [4, 8], [4, 3], [2, 9], [2, 5], [5, 6], [5, 7], [7, 99], [7, 9], [9, 8], [9, 10], [6, 10], [3, 7]]
# arr = [list(map(int, input().split())) for _ in range (E)]
'''

for tc in range(10):
    T, n = map(int,input().split())
    b = 99  # 도착지
    lst = list(map(int, input().split()))
    adj = []
    # 슬라이싱으로 2차원 배열 만들기
    for i in range(len(lst)):
        if i % 2 == 0:
            adj.append(lst[i:i+2])

    # 0 으로 된 행렬 만들기 도착점이 99!
    arr = [[0]*(b+1) for _ in range(b+1)]

    # 경로가 있는 곳에 1 표시된 행렬
    for i in adj:
        arr[i[0]][i[1]] = 1

    # 이제 시작
    a = 0  # 출발지
    visited = [0] * (100)  # 방문한 곳 표시
    visited[a] = 1  # 시작점 표시
    stack = []  # 현재 노드 저장
    ans = 0  # 경로 존재하면 1
    while ans != 1:
        for w in range(1, b+1): # w 는 다음 방문 지점.
            if arr[a][w] == 1 and visited[w] == 0:  # 노드가 연결되어있고 and 방문한적 없으면
                stack.append(a)  # 현재 위치 경로로 저장
                a = w  # 다음으로 이동
                visited[a] = 1  # 방문체크!
                if a == b:  # 도착지 경로 존재하면
                    ans = 1
                    break
                else:
                    ans = 0
                break
        else: # 방문한 적 있고, stack에 이전 경로 있으면
            if stack:
                a = stack.pop()  # 이전 경로로 돌아가기.
            else:
                break

    print(f'#{T} {ans}')


