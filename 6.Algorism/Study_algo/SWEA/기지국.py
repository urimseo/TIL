'''
t = int(input())
1
9
XXXXXXXXX
XXXHXXXXX
XXHBHXXHX
XXHHXXXXX
XXXXXXXXX
XXCHHXXXX
XXHXXHAHX
XXBHXXHXX
XXHXHXXXX
#1. 입력을 받는다. 리스트의 형태로 ..
N = int(input())
ARR = [list(input()) for _ in range(N)]

print(ARR)

#2.nXn행력에서 지운다: '-'
for i in range(N):
    for j in range(N):
        if ARR[i][j] == 'H' or ARR[i][j] == 'X' or ARR[i][j] == '-':
            continue

        if ARR[i][j] == 'A':
            k = 1
        elif ARR[i][j] == 'B':
            k = 2
        elif ARR[i][j] == 'C':
            k = 3

        for k in range(1, k+1):
            if 0<=i-k: ARR[i-k][j] = '-'
            if i+k<N: ARR[i+k][j] = '-'
            if j+k<N: ARR[i][j+k] = '-'
            if 0<=j-k: ARR[i][j-k] = '-'

cnt = 0
for i in range(N):
    for j in range(N):
        if ARR[i][j] == 'H':
            cnt += 1

print(ARR)
#4. 출력
print('#{} {}'.format(tc, cnt))

'''

for tc in range(1, int(input())+1):
    n = int(input())
    lst = [list(input()) for _ in range(n)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(n): # 행, 열 돌면서
        for j in range(n):
            if lst[i][j] == 'A':
                for a in range(4):
                    ni, nj = i + di[a], j +dj[a]
                    if 0<= ni < n and 0<= nj < n:
                        lst[ni][nj] = 'O'

            elif lst[i][j] == 'B':
                flag = 2
                while flag > 0:
                    for a in range(4):
                        ni, nj = i + di[a]*flag, j + dj[a]*flag
                        if 0 <= ni < n and 0 <= nj < n:
                            lst[ni][nj] = 'O'
                    flag -= 1 # flag 지워주기

            elif lst[i][j] == 'C':
                flag = 3
                while flag > 0:
                    for a in range(4):
                        ni, nj = i + di[a]*flag, j + dj[a]*flag
                        if 0 <= ni < n and 0 <= nj < n:
                            lst[ni][nj] = 'O'
                    flag -= 1 # flag 지워주기



    cnt =0
    for r in range(n):
        for c in range(n):
            if lst[r][c] == 'H':
                cnt += 1
    print('#{} {}'.format(tc, cnt))


