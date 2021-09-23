'''
# 상우하좌
dr = [-1, 0, 1, -1] # 행
dc = [0, 1, 0, -1] #열
da = [-1, 1, 1, 0] #대각
db = [1, 1, -1, -1]

n = 5
arr = [[' ']*n for _ in range(n)]
r = c = 5 #(5, 5)
for i in range(4):
    nr, nc = r + dr[i], c + dc[i]

    while 0 <= nr <= n and 0<= nc < n:
        arr[nr][nc] = i
        # 적고 바꾸고 적고 바꾸고 기록하면서...
        nr, nc = nr + dr[i], nc + dc[i]

for lst in arr:
    print(*lst)
'''
# 아래로향하는 방향
dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]

def check(r, c):
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        cnt = 1
        while 0 <= nr <= n and 0 <= nc < n and board[nr][nc] == 'o':
            cnt += 1
            nr, nc = nr + dr[i], nc + dc[i]
        if cnt > 4:
            return 1
    return 0

string = ['NO', 'YES']
n = int(input())
board = [[' ']*n for _ in range(n)]

ans = 0
for r in range(n):
    for c in range(n):
        if board[r][c] == '.' :continue
        ans = check(r, c)
        if ans: break
    if ans:break

print(string(ans))
