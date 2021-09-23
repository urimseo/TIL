'''
델타배열로 해보기
'''
n = int(input())
lst = [list(map( int, input().split())) for _ in range(n)]
res = 0  # 교착
for j in range(n):
    cnt = 0 # 내려오는것
    for i in range(n):
        if lst[i][j] == 2:  # s로 내려가야함.
            cnt = 1
        if lst[i][j] == 1 and cnt:  # n극으로 올라오는거 만났는데, 내려가는게 있으면
            res += 1 # 교착상태 하나 증가
            cnt = 0 # 내려오는거 없다고 가정 이미 교착 더했기 때문

print(res)