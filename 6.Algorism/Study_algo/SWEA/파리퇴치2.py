t = int(input())
for tc in range(1, t+1):

    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            res = 0 # 영역별 파리 개수
            # 돌면서 구간을따로 이렇게 나눠서 여기서 우대각 좌대각 정하기
            for a in range(m):
                res += lst[a+i][a+j] # 우대각
                res += lst[a+i][m-1-a+j] # 좌대각

            if m % 2: # 홀수면 대각선 겹쳐서 중간값 빼주기
                res -= lst[i + m//2][j + m//2]
            if res > maxV:
                maxV = res

    print(f'#{tc} {maxV}')