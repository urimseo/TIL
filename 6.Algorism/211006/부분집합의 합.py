#########재귀풀이 1번############
def f1(i, N): # i 번 원소가 포함되는 경우 N 개
    if i == N: # 모든 원소에 대한 고려가 끝난 경우 하나의 부분집합이 생성된 것임.
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
        if s == 10:
            for j in range(N):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        bit[i] = 0
        f1(i+1, N)
        bit[i] = 1
        f1(i+1, N)

############재귀풀이 2번#################
def f2(i, N, s):   # i 번 원소가 포함되는 경우 N 개
    if i == N:    # 모든 원소에 대한 고려가 끝난 경우 하나의 부분집합이 생성된 것임.
        if s == 10:
            for j in range(N):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    elif s > 10:
        return ## 만약 s가 1을 넘어갔으면 중단
    else:
        bit[i] = 0
        f2(i+1, N, s)
        bit[i] = 1
        f2(i+1, N, s+A[i])

# bit = [0]*10
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# f1(0, 10)
# f2(0, 10, 0)

############길이 줄어드는거 확인
def f3(i, N, s, rs):   # i 번 원소가 포함되는 경우 N 개
    global cnt
    cnt += 1
    if i == N:    # 모든 원소에 대한 고려가 끝난 경우 하나의 부분집합이 생성된 것임.
        if s == 50:
            for j in range(N):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    # elif s  > 10:
    #     return ## 만약 s가 1을 넘어갔으면 중단
    elif s + rs < 50:
        return
    else:
        bit[i] = 0
        f3(i+1, N, s, rs-A[i])
        bit[i] = 1
        f3(i+1, N, s+A[i], rs-A[i])

bit = [0]*10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = 0
# f1(0, 10)
# f2(0, 10, 0)

# f3(0, 10, 0, sum(A))
# print(cnt)


for i in range(1, 1<<10): #공집합 빼고 # i 가 한개의 부분집합 구성을 나타냄
    s = 0                              # i 가 나타내는 부분집합의 합
    for j in range(10):
        if i &(1<<j): # j번 비트가 1이라면 (A[j]가 부분집합에 포함된 경우
            s += A[j]
    if s == 10:
        for j in range(10):
            if i & (1 << j):
                print(A[j], end=' ')  # 현재의 부분집합 표시
        print()