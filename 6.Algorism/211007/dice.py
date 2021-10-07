'''
주사위 던지기 게임
- 정사면제 1~4 까지 4개 -> n번 던진다.
- n 번 던져서 나올 수 있는 경우의 수
ex. n = 3  111, 112, 113, ...~ 443, 444 까지 나옴
 재귀호출 통해서 주사위 던지기 만들기
'''

### 중복 불가능하게 만들기 - 순열
# def func(level, path):
#     if level == N:  # N은 전제조건. 바닥조건/ 0 1 2 ...N-1
#         print(path)
#         return
#
#     for i in range(1, 4+1):
#         if not visited[i]:
#             visited[i] = 1
#             func(level + 1, path+str(i))
#             visited[i] = 0
#     return
#
# N = 3
# visited = [0] * (N+2)
# func(0, "")


### 중복 불가능하게 만들기 - 순열2
def func(level):
    if level == N:  # N은 전제조건. 바닥조건/ 0 1 2 ...N-1
        for i in range(N):
            print(path[i], end='')
        print()
        return

    for i in range(1, 4+1):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = i  # 전체 level 에서 i 눈금 선택
        func(level + 1)
        path[level] = 0  # 원상복구 (필수 아님)
        used[i] = 0  #
    return
# 원상복구 헷갈리면 tree 꼭 그려서 확인하기 !!!


N = 3
path =[0]*N*3
used = [0] * (N+1)  # 인덱스 1~4까지 이용
func(0)


'''  #  중복 가능하게 만들기 
def func(level, path) :
    if level == N : # 0 1 2 ... N-1 / 바닥조건 , 기저조건
        print(path)
        return
    for i in range(1,4+1):
        func(level + 1, path+ str(i))
    return
N = 5
func(0,"")
'''

'''
def func(level) :
    if level == N :
        for i in range(N):
            print(path[i], end ='')
        print()
        return
    for i in range(1, 4+1):
        if used[i] == 1 : continue # 가지치기 ( 이전 재귀호출에서 i눈금 선택)
        used[i] = 1
        path[level] = i # 현재 level 에서 i 눈금 선택
        func(level + 1)
        path[level] = 0 # 원상복구 (필수는아님)
        used[i] = 0 # 원상복구 (헷갈리시는 분은 used 상태트리를 꼭 그려보기 )
    return
N = 3
path = [0,0,0,0,0,0,0]
used = [0] * (4+1) # [1] ~ [4]
func(0)
'''