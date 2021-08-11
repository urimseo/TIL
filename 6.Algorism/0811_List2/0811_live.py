'''
# 2차원 리스트 입력받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

arr2 = [[0] * M for _ in range (N)]
print(arr2)
# arr2 = [[0]]*M*N -> 사용하면 절대 안됨..!!
# 하나의리스트를 2개가 가리키는 형태임.

'''

#############################
'''
델타를 이용한 2차원 배열 탐색


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
# print      arr[ni][nj]
            # 만약 i,j 가 왼쪽 모서리에 있으면 index error나기 때문에 조건 붙여야함
            if 0 <= ni < N and 0 <= nj < M: # 배열을 벗어나지 않으면,
                arr[ni][nj]


for i in range(N):
    for j in range(M):
        for dr, dc in [[0,1], [1, 0], [0, -1], [-1, 0]]: # 모든 칸의 좌표 계산
            ni = i + dr
            nj = j + dr
            if 0 <= ni < N and 0 <= nj < M:
                arr[ni][nj]
'''

##################################
'''
 **정렬되어있지 않은 경우 탐색**
-> 검색 성공
def search(A, N, key):
    for i : 0-> N-1:
        if A[i] ==key:
            return True

    -> 검색 실패면 for문 그냥 종료됨
    return false


**정렬된 경우 탐색**
for i : 0 -> n-1:
    if a[i] == key
        return i
    elif a[i] > key
        return -1

return -1
'''

'''
**이진탐색**
2 4 7 9 11 19 23
'''

#
# def binarySearch(a, key):
#     start = 0
#     end = len(a) - 1
#     while start <= end:
#         middle = (start + end) // 2
#         if a[middle] == key:
#             return middle
#         elif a[middle] > key:
#             end = middle - 1
#         else:
#             start = middle + 1
#     return -1
#
#
# a = [2, 4, 7, 9, 11, 19, 23]
# print(binarySearch(a, 11))  # 4  검색 성공하면 index 반환
# print(binarySearch(a, 10))  # -1 검색 실패했으니 return -1

TC = int(input())

for tc in range(TC):
    N = int(input())  # 3
    Arr = [[0 for i in range(N)] for j in range(N)]

    # print(Arr)  #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # 초기값들
    di = [0, 1, 0, -1]  # di와 dj의 인덱스 위치로 쓸 k는 0,1,2,3 안에서 순환되어야 함.
    dj = [1, 0, -1, 0]  # 시계방향으로 돌아야 하므로, 인자들은 이 값 순서대로.
    ci, cj = 0, -1  # for문을 써서 모든 i에 대해 모든 j를 보고 넘어갈 것이 아니므로, 수동 초기값 설정
    ni, nj = 0, 0  # 다음에 이동할 위치 0, 0 설정 (첫번째 while문 돌때, 초기 ci, cj, di, dj값 그대로 반영하게끔)

    cnt = 1
    k = 0  # k도 처음에 방향이 dr안에 0인덱스.

    while cnt <= N * N:  # N*N이내면, while문을 돌린다.
        ni = ci + di[k]  # 새로 이동할 위치 ni, nj를 초기값기준 ci+di[0], ci+di[0]인 0+0, 0+1 로 이동
        nj = cj + dj[k]

        # 1. 새로 도달할 위치가 Arr안에 위치하고 & 0값이 있어야. (아무 1이상의 cnt가 찍히지 않은 자리어야)
        if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and Arr[ni][nj] == 0:  # N-1로 인덱스 마지막값으로 적는 것 주의
            Arr[ni][nj] = cnt  # 카운트값을 그 새 칸에 할당
            cnt += 1  # 하나 썼으니까, 카운트값 하나 증가시켜주고
            ci, cj = ni, nj  # 새로운 좌표 계산할 이전 값을 갱신해줌. 이제 ci, cj가 0, 1이 되고(current i, j) 위에 while문 아래서 다시 갱신할 것

        # 2. 새로 도달할 위치가 배열 밖에 있거나 이미 1이상의 숫자가 찍힌 경우
        else:
            k = (k + 1) % 4  # di/dj안의 인덱스는 0에서 4사이로 돌아야 하므로

    print(f'#{tc + 1}')
    for i in Arr:  # i는 Arr:[[*, *, *, *], [*, *, *, *], [*, *, *, *]]의 각 인자들이므로, [1, 2, 3, 4, 5]등의 리스트.
        for j in i:  # i: [*, *, *, *]안의 각 인자들에 대해
            print(j, end=' ')  # *를 옆칸에 프린트
        print()




















