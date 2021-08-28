t = int(input())
for tc in range(1, t+1):
    n, m= map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            res = 0
            for a in range(i, i+m):
                for b in range(j, j+m):
                    res += lst[a][b]
            if res > maxV:
                maxV = res
    print(f'#{tc} {maxV}')
