'''
델타배열로 해보기
'''
for tc in range(1, 11):
    n = int(input())
    lst = [list(map( int, input().split())) for _ in range(n)]

    total = 0  # 최종 교착
    for j in range(n):
        ni, nj = 0, 0
        cnt = 0 # 내려오는것
        res = 0  #교착
        for i in range(n-1):
            if lst[i][j] == 1:  # s로 내려가야함.
                ni, nj = i, j
                cnt = 1
                while ni < n-1:
                    ni, nj = ni+1, j  # 내려가면서 확인하는데
                    if lst[ni][nj] == 2 and cnt:  # n극으로 올라오는거 만났는데, 내려가는게 있으면
                        res += 1 # 교착상태 하나 증가
                        cnt = 0 # 내려오는거 없다고 가정 이미 교착 더했기 때문
                    elif lst[ni][nj] == 1:
                        cnt = 1
            total += res
            if res or cnt: # 어차피 행 전부 돌았으니 j만 이동 시켜야해서 break
                break # 그런데, 교착이 없을때도 일단    이동해야하니 Scnt
    print(f'#{tc} {total}')