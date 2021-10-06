'''
스토쿠
가로검사, 세로검사
벽, 끝자리에 도달 이면 k와 개수비교후 cnt +
1. 빈칸 -> 벽 일 때 cnt가 k?
2. 끝났을때 센 개수 -> k?
 끝났을때 -> 겉에 벽 만들기(list 추가).
 그럼 끝났을 떄 조건을 따로 주지 않아도됨.

7 3 6 4 8 9 2 5 1
8 5 2 7 3 1 6 9 4
9 1 4 5 6 2 7 3 8
4 9 7 2 5 6 8 1 3
5 6 3 1 8 7 9 4 2
2 8 1 9 4 3 5 6 7
6 7 5 3 2 4 1 8 9
1 4 9 6 7 8 3 2 5
3 2 8 1 9 5 4 7 6
'''

def Sudoku(lst_w, lst_h):
    count_w = [[0]*10 for _ in range(9)]
    count_h = [[0] * 10 for _ in range(9)]
    square = [[0] * 10 for _ in range(9)]
    for r in range(9):  # 0 ~ 9
        for c in range(9):  # 0 ~ 9
            count_w[r][lst_w[r][c]] += 1  # for r  for c
            count_h[r][lst_h[r][c]] += 1
            if r%3 ==0 and c %3 ==0:
                for x in range(r, r+3):
                    for y in range(c, c+3):
                        square[x][lst_w[x][y]] += 1  # square 는 앞에 인덱스가 필요 없다...
    # 이 for 

    for i in range(9):
        for j in range(1, 10):
            if count_w[i][j] != 1 or count_h[i][j] != 1 or square[i][j] != 1:
                return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    sudoku_w = [list(map(int, input().split())) for _ in range(9)]
    sudoku_h = [[0]*9 for _ in range(9)]

    # print(sudoku_w)
    for i in range(9):
        for j in range(9):
            sudoku_h[j][i] = sudoku_w[i][j]
    # print(sudoku_h)
    print(f'#{tc} {Sudoku(sudoku_w, sudoku_h)}')

