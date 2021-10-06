n = 4

lst = [[0]*n for _ in range(n)]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 총 4방향으로 꺾임
k = 0 # 첫번쨰 방향은 오르쪽
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
#시작인덱스
i, j = 0, -1
#다음에 갈 인덱스
ni, nj = 0, 0
# 들어갈 숫자
tmp = 1
while tmp <= n*n:
    ni = i + di[k]
    nj = j + dj[k]
    if 0 <= ni <= n-1 and 0 <= nj <= n-1 and lst[ni][nj] == 0: 
        i, j = ni, nj
        lst[ni][nj] = tmp
        tmp+=1
    else:
        k = (k+1) % 4

for i in lst:
    print(*i)
print()
