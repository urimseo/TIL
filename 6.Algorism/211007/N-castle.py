'''
N-Queen 문제 변형
- 서로 공격하지 않는 경우의 수
- N 마리 castle 배치
- 경우의 수 백트래킹으로 출력하기
'''

# def chess(i, n):
#     if i == n:
#         return
#     else:
#         for j in range(n):
#             if lst[i]: continue
#             lst[i][j] = 1
#             chess(i+1, n)
#             lst[i][j] = 0
#

# n = 3
# lst = [[0]* n for _ in range(n)]
# chess(0, n)

# 가로 라인 겹치지 않게
# def func(y):
#     if y == N:
#         return
#     for x in range(N):
#         MAP[y][x]='#'
#         func(y+1)
#         MAP[y][x] = '_' # 원상복구
# N = 4
# MAP = [
#     ['_' for _ in range(N)] for _ in range(N)
# ]  # debugging  용도
# func(0)


## 세로라인 겹치지 않게
def func(y):
    global cnt
    if y == N:
        cnt += 1 # 경우의 수가 하나 만들어졌을 때 counting 하게된다
        return
    for x in range(N):
        if used[x] == 1 : continue
        used[x] = 1
        MAP[y][x]='#'
        func(y+1)
        MAP[y][x] = '_' # 원상복구
        used[x] = 0
N = 4
MAP = [
    ['_' for _ in range(N)] for _ in range(N)
]  # debugging  용도
used = [0] * N  # x 좌표 사용 체크
func(0)


'''
def func(y):
    global cnt
    if y == N :
        cnt += 1 # 경우의 수가 만들어졌을때 카운팅
        return
    for x in range(N):
        if used[x] == 1 : continue # 이전에 x 좌표 사용 , 가지치기
        used[x] = 1
        MAP[y][x] = '#' # (y,x) 선택
        func(y + 1)
        MAP[y][x] = '_' # 원상복구
        used[x] = 0
N = 4
MAP = [
    ['_' for _ in range(N)] for _ in range(N)
] # debugging 용도
cnt = 0
used = [0] * N # x 좌표 사용 체크
func(0)
print(cnt)
'''