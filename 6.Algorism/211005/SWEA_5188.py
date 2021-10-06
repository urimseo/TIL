'''
최소합
- 각 칸에서는 오른쪽이나 아래로만 이동 가능
di ,dj 설정해서 : 오른쪽/아래 유효성 비교
- 오른쪽 없으면 아래로
- 아래 없으면 오른쪽으로
- 둘 다 있으면 값 비교해서 작은쪽으로


- 경로횟수 : 무조건 n*2-2
- 0101 로 가능한. 모든 부분집합 생성..?
-

'''

def f(n, m, k):
    if n == k:
        one = p[::]
        if one not in total:
            total.append(one)

    else:
        for i in range(m):  #
            if u[i] == 0:  # 가장작은자리부터 쓰지 않은 u
                u[i] = 1  # u를 사용처리
                p[k] = arr[i]  # p 에다가 넣기
                f(n, m, k + 1)
                u[i] = 0  # u 초기화

for tc in range(1, int(input())+1):
    n = int(input())
    nav = [list(map(int, input().split())) for _ in range(n)]

    total = []  # 전체 순열 합칠것
    way = (n * 2 - 2)
    arr = [0] * way + [1] * way
    p = [0] * way  # 빈배열 만들기
    u = [0] * len(arr)  # 사용했는지 확인할 used 배열
    f(way, len(arr), 0)

    # 0 이면 아래로, 1 이면 오른쪽으로
    # 아래 (1, 0), 오른쪽 (0,1)
    minV = 10*n*n
    for go in total:
        di = 0
        dj = 0
        res = 0
        res += nav[0][0] # 시작점 더하고

        # while di != n and dj !=n : # 오른쪽 끝에 도달하기 전까지
        for i in go:
            if i == 0: # 아래로
                di += 1
                if di < n: # 아래로 움직이니까 dj 만 검사
                   res += nav[di][dj]
                # 만약 끝에 도달했지만, 오른쪽으로 남아있을 경우가 있어 그러면
                else:
                    di, dj = di-1, dj +1
                    res += nav[di][dj]
            else:
                dj += 1
                if dj < n: # 아래로 움직이니까 dj 만 검사
                   res += nav[di][dj]
                # 만약 끝에 도달했지만, 오른쪽으로 남아있을 경우가 있어 그러면
                else:
                    di, dj = di + 1, dj - 1
                    res += nav[di][dj]
        if minV > res:
            minV = res
    print(f'#{tc} {minV}')

# N = len(lst)

# for i in range(1, 1<<N):
#     arr = []
#     for j in range(N):
#         if i & (1 << j):
#             arr.append(lst[j])
#     if len(arr) == way:
#         if not arr in total:
#             total.append(arr)
# 여기서 순열 만들기