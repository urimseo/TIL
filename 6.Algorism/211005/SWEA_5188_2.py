di = [1, 0]
dj = [0, 1]

def dfs(i, j, res):
    global minV
    if i == n-1 and j == n-1:
        if res < minV:
            minV = res
    else:
        for k in range(2):
            ni, nj = i + di[k], j + dj[k]
            if 0<= ni < n and 0 <= nj < n:
                dfs(ni, nj, res+arr[ni][nj]) # 시작점 변경해서 재호출

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    minV = n*n*10  # 최소값
    dfs(0, 0, arr[0][0]) # 시작점 i,j / 초기값 res에 더한채로 시작 
    print(f'#{tc} {minV}')
