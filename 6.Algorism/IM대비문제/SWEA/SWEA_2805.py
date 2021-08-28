'''
n -> 배열의 크기
split = 2//n
for i -> 0-> split
    for j -> split -i, split+i+1까지
    더해

그리고 중간열 전부 더해야 하니까..
for i in range(2//n, n) # 중간부터 끝까지
    for j -> (n, -1, 2)  # 5 3 1인데..
'''
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input())) for _ in range(n)]
    res = 0
    mid = n//2
    for r in range(0, mid):
        for c in range(mid-r, mid+r+1):
            res += lst[r][c]
    idx = 0
    # 중간부터 아래 리스트 탐색
    for i in range(n//2, n):  # i++
        for j in range(idx, n-idx): # j--
            res += lst[i][j]
        idx += 1 # 인덱스로 j 범위 줄여줌
    print(f'#{tc} {res}')






