T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    result = [] # 모든 합이 들어가는 리스트
    #  행, 대각선의 합 구하기
    for j in range(100):
        i_total = 0  # 행의 합
        rd_total = 0  # 오른쪽 대각합
        ld_total = 0  # 왼쪽 대각 합
        for i in range(100):
            i_total += lst[i][j]
            rd_total += lst[i][i] # 값이 1개이기 때문에 나중에 더함
            ld_total += lst[i][100-1-i]
        result.append(i_total)
    # 열의 합 구하기
    for i in range(100):
        j_total = 0
        for j in range(100):
            j_total += lst[i][j]
        result.append(j_total)
    # 대각선 2개의 값 리스트에 추가
    result.append(rd_total)
    result.append(ld_total)

    print(f'#{N} {max(result)}')

