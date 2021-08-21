T = int(input())
for tc in range(1, T+1):
    sudoku_w = [list(map(int, input().split())) for _ in range(9)]
    sudoku_h = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            sudoku_h[j][i] = sudoku_w[i][j]
    res = 0 # res = 0 이면 스토쿠 검증 실패.
    while res == 0:
        for i in range(9):  # 총 9번 반복
            res = 1 # 일단 res =1 이고, 틀리면 res = 0이라 while문 종료
            count_w = [0] * 10
            count_h = [0] * 10
            square = [0] * 10
            for j in range(9):  # 한행마다
                numa = sudoku_w[i][j]
                numb = sudoku_h[i][j]
                if count_w[numa]: # 이미 있는 숫자가 중복되는 경우
                    res = 0 # 검증 실패.
                else:
                    count_w[numa] = 1
                if count_h[numb]:
                    res = 0
                else:
                    count_h[numb] = 1

                if i%3 == 0 and j%3 == 0: #사각형 검증하기 위해서 0 3 6 에서 끊어서 검증
                    square = [0] * 10
                    for r in range(i, i+3): # 0~3 , 3~6
                        for c in range(i, i+3):
                            nums = sudoku_w[r][c]
                            if square[nums]:
                                res = 0
                            else:
                                square[nums] = 1
            if res == 0:
                break
        if res == 0:
            break
    print(f'#{tc} {res}')




