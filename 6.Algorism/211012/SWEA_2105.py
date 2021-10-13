'''
디저트 카페
- 대각선으로 이동하면서 직사각형 경로 그리기
di = [1, 1, -1, -1]  #우하, 좌하, 좌상, 우상
dj = [1, -1, -1, 1]
- 단, 출발한 카페로 돌아와야 한다.


- 경로상에 있는 값이 중복되면 안됨

- 경로의 최대 길이 구하기

# getsqare(시작지점, w, h)
시작지점부터 사각형의 길이를 얻어주는 함수 구하기
경로 길이

# go 함수
# 같은 경로상에서 똑같은 숫자가 나오면 안된다.
# 탐색을 하면서 기록할 used 배열
# 사각형 그리면서 used check
'''
#우하, 좌하, 좌상, 우상
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

# def check(i, j, n, move):
#       # 디저트 종류 체크
#     visited[lst[i][j]] = 1
#     ni = i + di[move]
#     nj = j + dj[move]
#     de = lst[ni][nj]
#     if 0<= ni<n and 0<= nj<n and visited[lst[ni][nj]] == 0:  # 범위를 벗어나지 않고, 있다면
#         visited[lst[ni][nj]] = 1
#         if 0<= ni+di[move]<n and 0<= nj+dj[move]<n and visited[lst[ni][nj]] == 1:
#             check(ni, nj, n, move+1)
#         elif 0<= ni+di[move]<n and 0 <= nj+dj[move] <n and visited[lst[ni][nj]] == 0:
#             check(ni, nj, n, move)

def go(r, c, length, k):
    global n
    global used
    cnt = 0  # 경로 cnt
    for i in range(length):
        r = r+dr[k]  # 이 방향으로 탐색하겠다
        c = c+dc[k]
        # 범위내에 있는지 확인
        if r < 0 or c < 0 or r >= n or c >= n: return -1, -1, -1
        if used[lst[r][c]]: return -1, -1, -1
        used[lst[r][c]] = 1
        cnt += 1
    return r, c, cnt



def get_squre(r, c, height, width):
  # 1 ~ 100 까지 사용
    sumV = 0  # 경로 개수 카운팅
    for t in range(4):
        if t == 0 or t ==2:
            r, c, temp_sum = go(r, c, height, t)  # 오른쪽 대각선 - 세로길이 사각형 만들기
        else:
            r, c, temp_sum = go(r, c, width, t)  # 왼쪽 대각선 - 가로길이 사각형 만들기
        if temp_sum == -1: return -1   # 만약 갈 수 없는 길로 return 되면 그냥 -1 return 하기
        else:
            sumV += temp_sum

    return sumV
    # 우하 방향 먼저 탐색

for tc in range(1, int(input())+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n-1):  # 시작 인덱스 i, j
        for j in range(1, n-1):
            for k in range(1, n-1): # 움직일 사각형의 가로길이
                for kk in range(1, n-1): # 세로길이
                    used = [0] * 101
                    res = max(get_squre(i, j, k, kk), res)

    if not res:
        res = -1

    print(f'#{tc} {res}')



'''
dr = [1,1,-1,-1]
dc = [1,-1,-1,1]
def go (r, c, length , t ,used):
    cnt = 0
    for i in range(length - 1):
        r = r + dr[t]
        c = c + dc[t]
        if r < 0 or c < 0 or r >= 5 or c >= 5 : return -1,-1,-1# 범위 바깥인지?
        if used[MAP[r][c]] == 1 : return -1,-1,-1
        used[MAP[r][c]] = 1
        cnt += 1
    return r,c, cnt
def get_square(r,c, height, width) :
    used = [0] * 101 # 1 ~ 100
    sum = 0
    for t in range(4) :
        if t == 0 or t == 2 :
            r,c,temp_sum = go(r,c,height, t)
        else :
            r,c, temp_sum = go(r,c,width, t)
        if temp_sum == -1 : return -1
        else :
            sum += temp_sum
    return sum # 경로 길이
MAP = [
    [9 ,8 ,9 ,8 ,1],
    [4 ,6 ,9 ,4 ,1],
    [8 ,7 ,7 ,8 ,1],
    [4 ,5 ,3 ,5 ,9],
    [4 ,5 ,3 ,5 ,2],
]
ret = get_square(1,2,3,2)
print(ret)

'''