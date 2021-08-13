
for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    i, j = 99, arr[99].index(2)  # 내위치
    ni, nj = 0, 0  # 이동할 위치
    # [상, 우, 좌] 순서
    dj = [0, 1, -1]
    res = 0

    while i != 1:  # 명백한 조건 넣어주기.
        for x in range(i-1, -1, -1):  # x는 위로 올라가면서 확인 , 2가 있는 윗줄부터 탐색 시작(i-1)
            for y in range(0, 99, 1):  # y는 왼쪽으로 가면서 확인
                ni = i - 1  # '현재 기준점 위치 + 위로 올라가야함.
                nj = j

                # 오른쪽에 1이 있으면, 방향을 바꿔
                if nj < 99 and arr[ni][nj + 1] == 1 and stop != 2:  # 현재가 i, j 근데 방향을 바꿔서 가다가 0을 만나면 ..? 위로 올라가야 한다.!
                    j = j + 1  # 오른쪽으로 이동해서 다시반복.
                    stop = 1
                    if nj+1 == 0:
                        i = i - 1
                        break

                elif nj > 0 and arr[ni][nj -1] == 1 and stop != 1:  # 왼쪽 바라보고
                    nj = j - 1
                    stop = 2
                    if nj - 1 == 0:
                        i = i - 1
                        break

                elif 0 <= nj <= 99 and ni != 0:
                    i = i - 1
                    stop = 0
                elif i == 1:
                    res = nj

    print(f'#{T} {res}')
