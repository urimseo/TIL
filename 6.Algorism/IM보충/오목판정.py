'''
N X N 크기의 판이 있다.
 판의 각 칸에는 돌이 있거나 없을 수 있다.
 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.
'''
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [list(input()) for _ in range(n)]

    cnt1, cnt2, res1, res2 = 1, 1, 0, 0 # 행
    for i in range(n):
        for j in range(n):
            if i
    print(res1, res2)






    # minv = 0
    # cnt3 = 1 #우대
    # cnt4 = 1 #좌대
    # res = 'NO'
    # for i in range(n-1): #행
    #     if lst[i][i] == 'o' and lst[i+1][j+1] == 'o':
    #         cnt3 += 1
    #     else:
    #         res = cnt
    #         cnt = 0
    #     if lst[i][n-1-i] == 'o' and lst[i][n-i] == 'o':
    #         cnt4 += 1
    #
    #     cnt1 = 1  # 행
    #     cnt2 = 1  # 열
    #     for j in range(n-1):#열
    #         if lst[i][j] =='o' and lst[i][j+1] == 'o':
    #             cnt1 += 1
    #         else:
    #             cnt = 0
    #         if lst[j][i] == 'o':
    #             cnt2 += 1
    #     if cnt1 >= 5 or cnt2 >= 5:
    #         res = 'YES'
    #         break
    # if cnt3 >= 5 or cnt4 >= 5:
    #     res = 'YES'
    #
    # print(f'#{tc} {res}')


