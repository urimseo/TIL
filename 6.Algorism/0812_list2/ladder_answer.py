'''

1. 왼쪽칸이 1이면
2. 오른쪽 칸이 1이면
'''

def search(start):
    i = 99
    j = start
    while i > 0:
        i -= 1  # 위로 한칸 이동

        # 왼쪽이 1이면 0을 만날때까지 이동.
        if j > 0 and ladder[i][j-1] == 1:
            while j > 0 and ladder[i][j-1] == 1:
                j -= 1
        # 오른쪽이 1이면 0을 만날때까지 이동
        elif j < 99 and ladder[i][j+1] == 1:
            while j < 99 and ladder[i][j+1] == 1:
                j += 1
    return j



for tc in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    goal = ladder[99].index(2)

    ans = search(goal)
    print(f'#{T} {ans}')
