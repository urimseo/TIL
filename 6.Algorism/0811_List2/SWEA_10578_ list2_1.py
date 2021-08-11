T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            # 이걸 k in range(4)로 하고, 밖에 di, dj 별도로 선언 가능
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i+di, j+dj  # 시계방향순으로 주변의 인덱스 값이 나옴
                if 0 <= ni < N and 0 <= nj < N:  # 배열을 벗어나지 않을 경우
                    ans += abs(arr[i][j] - arr[ni][nj])
    print(f'#{tc+1} {ans}')


