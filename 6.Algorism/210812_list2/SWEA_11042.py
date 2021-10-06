t = int(input())
for tc in range(1, t+1):
    N, n, m = map(int, input().split())
    # N개의 배열 내 n * m 의 부분배열의 합
    lst = [list(map( int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N-n+1):
        for j in range(N-m+1):
            res = 0
            for ni in range(n):
                for mj in range(m):
                    a = i +ni
                    b = j +mj
                    res += lst[i+ni][j+mj]
            if res > maxV:
                maxV = res
    print(f'#{tc} {maxV}')