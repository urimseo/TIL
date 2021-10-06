'''

1. 왼쪽칸이 1이면
2. 오른쪽 칸이 1이면
'''

# def search(start):
#     i = 99
#     j = start
#     while i > 0:
#         i -= 1  # 위로 한칸 이동
#
#         # 왼쪽이 1이면 0을 만날때까지 이동.
#         if j > 0 and ladder[i][j-1] == 1:
#             while j > 0 and ladder[i][j-1] == 1:
#                 j -= 1
#         # 오른쪽이 1이면 0을 만날때까지 이동
#         elif j < 99 and ladder[i][j+1] == 1:
#             while j < 99 and ladder[i][j+1] == 1:
#                 j += 1
#     return j
#
#
#
# for tc in range(10):
#     T = int(input())
#     ladder = [list(map(int, input().split())) for _ in range(100)]
#
#     goal = ladder[99].index(2)
#     print(goal)
#
#     ans = search(goal)
#     print(f'#{T} {ans}')
for tc in range(10):
    T = int(input())  # 테스트 케이스 넘버
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]  # 2차원 배열 사다리

    for i in range(N):
        if arr[99][i] == 2:  # 도착 지점의 x 인덱스 찾기
            y = i
            break

    x = 99
    while x != 0:  # 출발선에 도착하기 전까지
        if 0 <= y - 1 and arr[x][y - 1] == 1:  # 왼쪽으로 이동
            arr[x][y] = 0
            y = y - 1


        elif y + 1 < 100 and arr[x][y + 1] == 1:  # 오른쪽으로 이동
            arr[x][y] = 0
            y = y + 1

        else:  # 좌우로 이동할 데가 없으면
            arr[x][y] = 0
            x = x - 1

    print(f'#{tc + 1} {y}')