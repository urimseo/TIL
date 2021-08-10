T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    min_num = sum(numbers)
    max_num = 0

    # 마지막 넘어가는 구간을 제외하고 반복
    for i in range(N - M + 1):
        tmp_sum = 0

        # 해당하는 구간만큼 반복하여 합 구하기
        for j in range(M):  # 0 1 2 3
            tmp_sum += numbers[i+j]

        if tmp_sum > max_num:
            max_num = tmp_sum
        if tmp_sum < min_num:
            min_num = tmp_sum

    print(f'#{tc} {max_num - min_num}')






