

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    res = 0
    for i in range(len(lst)): # 범위로 접근!!!!!!!
        for j in range(len(lst[i])):
            for k in range(4): #4 방향이기 때문에 range 4
                ni = i + di[k]  # 인덱스를 바꾸는것
                nj = j + dj[k]
                if 0 <= ni <= n-1 and 0 <= nj <= n-1: # 인덱스 오류 안나게 조심. 꼭 확인해야한다
                    res += abs(lst[i][j] - lst[ni][nj])

    print(f'#{tc} {res}')

