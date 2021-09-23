'''
오목판정
모든 리스트 돌면서
만약 , o 이 나오면 거기서부터 좌, 우 살피고
또, x를 살펴서
if o 이면 ++
. 이면 거기서 5보다 cnt가 크면  yes!!! 아니면  no
flag는 0을 기본으로 하고 찾으면 1이될 수 있도록 한다.
'''
for tc in range(1, int(input())+1):
    n = int(input())
    lst = [list(input()) for _ in range(n)]
    # + 우하
    flag = 0
    di = [0, 1, 1, 1]
    dj = [1, 0, 1, -1]
    # x 하우, 하좌
    # dr = [1, 1]
    # dc = [1, -1]
    # nr, nc = i + dr[k]*plus, j + dr[k]*plus
    for i in range(n):  # 모든 lst 돌면서
        if flag == 1:
            break
        for j in range(n):
            if flag == 1:
                break
            else:
                if lst[i][j] == 'o':
                    plus = 1
                    for k in range(4):
                        cnt = 1 # 방향이 바뀔때 cnt 시작
                        ni = i + di[k]
                        nj = j + dj[k]
                        while 0 <= ni < n and 0 <= nj < n and lst[ni][nj] == 'o':
                            cnt += 1
                            ni = ni + di[k]
                            nj = nj + dj[k]
                        if cnt > 4:
                            flag = 1 # 찾았으면 끝
                            break
    if flag == 1:
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))