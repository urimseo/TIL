T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # [[1, 3], [2, 5]]  a1, b1 / a2, b2 = bj
    P = int(input())

    stations = []  # 정류장
    for _ in range(P):
        stations.append(int(input()))
    # [1, 2, 3, 4, 5]

    # 카운팅 배열
    count = [0] * 5001
    for i in lst:
        for j in range(i[0], i[1]+1):
            count[j] += 1

    print(f'#{tc}', end=' ')
    for i in stations:
        print(count[i], end=' ')
    print()
