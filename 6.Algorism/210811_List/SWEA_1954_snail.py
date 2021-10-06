T = int(input())
for tc in range(T):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    # 우하좌상 방향
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i, j = 0, -1  # 현재 기준점이 되는 시작 위치
    ni, nj = 0, 0  # 다음에 이동할 위치

    tmp = 1  # 들어가야 값의 시작
    k = 0  # 방향을 표시하기 위한 변수 -> 나중에 인덱스 값으로 사용

    while tmp <= n * n:  # 배열 안에 들어갈 수 있는 수의 범위만큼반복 (ex. 3*3 -> 1~9까지)
        ni = i + di[k]  # '현재 기준점 위치 + 우로 이동하는 방향 ++ '은 다음 이동할 위치
        nj = j + dj[k]

        # 현재 위치가 상자 밖으로 나가지 않고 N-1범위 안에 있을떄
        # and arr의 리스트는 모두 0밖에 들어있지 않기 때문에 값(tmp)을 넣을때
        # 0이면 다른 값이 들어있지 않은 상태여서 값을 넣을 수 있다.
        if (0 <= ni <= n - 1) and (0 <= nj <= n - 1) and arr[ni][nj] == 0:
            i, j = ni, nj  # 위치 바꿔주고
            arr[i][j] = tmp  # 1부터 값 넣어주고
            tmp += 1  # 값을 증가한다.

        else:
            k = (k + 1) % 4  # 방향을 바꿔준다  1 2 3 0 순서로 나오면서 di, dx의 인덱스를 가리키게 됨.

    print(f'#{tc+1}')
    for a in range(n):
        print(' '.join(map(str, arr[a])))
