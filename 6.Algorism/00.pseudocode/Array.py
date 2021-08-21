'''
<2차원 배열>

**2차원 배열의 선언**
arr = [[0, 1, 2, 3][4, 5, 6]]

n = 개수
**2차원 배열의 입력**
arr = [list(map(int, input().split())) for _ in range(n)]

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

arr = [list(map(int, input().split())) for _ in range (E)]

**2차원 배열의 초기화 **
arr = [[0 for _ in range(n)] for _ in range(n)]

'''

'''
<배열 순회>

n * m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

array -> 2차원 배열
i -> 행의 좌표, j -> 열의 좌표
n -> len(array) - 행의 수  m -> len(array[i]) - 열의 수 

**행 우선 순회**

for i in range(n):
    for j in range (m):
        array[i][j]


**열 우선 순회**

for j in range(len(array[0])):
    for i in range(len(array)):
        array[i][j]
        
**지그재그 순회**

for i in range(len(array)):
    for j in range(len(array[0])):
        array[i][j + (m-1-2*j) * (i % 2)]
                   m-1 -> 열의수 2*j ->?????  i % 2 -> 짝수면 전체 0이어서 행정렬과 같아짐. 
                  
                  
                   
**델타를 이용한 2차 배열 탐색**

2차 배열의 한 좌표에서 4 방향의 인접 배열 요소를 탐색하는 방법.
- 만약 6 방향이라면, di, dj에 6개의 값을 넣어주고, k = 6
- 만약 8 방향이라면, di, dj에 8개의 값을 넣어주고, k = 8

# 우하좌상의 좌표 값
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
i, j -> 시작점
k = 4 -> 4방향이기 때문

for i in range(N):
    for j in range(M):
        for k in range(k):
            ni = i + di[k]
            nj = j + dj[k]
# print      arr[ni][nj]
            # 만약 i,j 가 왼쪽 모서리에 있으면 index error나기 때문에 조건 붙여야함
            if 0 <= ni < N-1 and 0 <= nj < M-1 : # 배열을 벗어나지 않으면,
                arr[ni][nj]


for i in range(N):
    for j in range(M):
        for dr, dc in [[0,1], [1, 0], [0, -1], [-1, 0]]: # 모든 칸의 좌표 계산
            ni = i + dr
            nj = j + dr
            if 0 <= ni < N-1 and 0 <= nj < M-1:
                arr[ni][nj]

** 전치 행렬**
i : 행의 좌표, len(arr)
j : 열의 좌표, len(arr[0])
n , m = 행의 수, 열의 수

##왼쪽 대각선  i == j 
for i in range(n):
    for j in range(m):
        if i < j:
            arr[i][j], arr[j,i] = arr[j][i], arr[i][j]

##오른쪽 대각선 i , j = n - 1 - i

for i in range(n):
    for j in range(m):
        if i < n - 1 - i:
            arr[i][j], arr[j,i] = arr[j][i], arr[i][j]
            
        









'''