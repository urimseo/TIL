'''
스도쿠
사각형 검사가 관건.
0~9 까지 중에 0`3, 3`6, 6`9를 확인.
i %3 == 0이면 3의 배수, 여기서부터 range(i, i+3,)까지

'''
n = int(input())
for tc in range(1, n+1):
    lst = [list(map(int, input().split())) for _ in range(9)]
    flag = -1 # flag가 -1이면 유효성 검증 실패
    while flag == -1:
        for i in range(9):
            tmp1 = []
            tmp2 = []
            for j in range(9):
                if lst[i][j] not in tmp1:
                    tmp1.append(lst[i][j])
                else:
                    flag = 0
                    break
                if lst[j][i] not in tmp2:#열검사
                    tmp2.append(lst[j][i])
                else:
                    flag = 0
                    break
                #square
                tmp3 = []
                if i%3 == 0 and j%3 == 0:
                    for r in range(i, i+3):
                        for c in range(j,j+3):
                            if lst[r][c] not in tmp3:  # 열검사
                                tmp3.append(lst[r][c])
                            else:
                                flag = 0
                                break
            if flag == 0:
                break
        if flag == 0:
            break
        else:
            flag = 1


    print('#{} {}'.format(tc, flag))