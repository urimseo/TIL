'''
정사각형 방
'''

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0
    maxcnt = 0
    visited = [0] * (n * n + 1)
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + di[k]
                nj = i + dj[k]

                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] - arr[i][j] == 1:
                        visited[arr[i][j]] = 1





