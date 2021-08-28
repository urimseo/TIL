'''
N X N 크기의 판이 있다.
 판의 각 칸에는 돌이 있거나 없을 수 있다.
 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.
'''
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [list(input()) for _ in range(n)]
    answer = ['NO', 'YES']
    res = -1
    cnt1, cnt2 = 0, 0
    # res가 1이면 반복문 나와서 종료
    # 대각선은 이런 반복문 안에서 아예 불가능인가...?
    #행, 열 비교는 여기서 가능
    while res == -1:
        for i in range(n):
            for j in range(n):
                if lst[i][j] == 'o':
                    cnt1 += 1
                else:
                    if cnt1 >= 5:
                        res = 1
                        break
                    else:
                        cnt1 = 0
                #열비교
                if lst[j][i] == 'o':
                    cnt2 += 1
                else:
                    if cnt2 >= 5:
                        res = 1
                        break
                    else:
                        cnt2 = 0
            if cnt1 >= 5 or cnt2 >= 5:  # 마지막값 따로 비교
                res = 1
                break

        # 대각선 비교 따로 해줘야함... while문 안에서 해보기
        # 우하대각, 좌하대각
        di = [1, 1]
        dj = [1, -1]
        for i in range(n):
            for j in range(n):
                for k in range(2):
                    if lst[i][j] =='o':
                        ni, nj = i + di[k], j + dj[k]  # 처음에 우선 위치를 이동하면서 'o'이 있나 없나 찾기
                        cnt = 1
                        while 0 <= ni < n and 0 <= nj < n and lst[ni][nj] == 'o':
                            cnt += 1  # while문 안에서 'o'이 아닐때까지 돌아야 하니까
                            ni, nj = ni + di[k], nj + dj[k]  # 내부에서 계속 + 해서 다음위치 이동시켜줘야함
                        if cnt > 4:
                            res = 1
                            break
        else:
            if res == -1:
                res = 0
                break
    print(f'#{tc} {res}')
