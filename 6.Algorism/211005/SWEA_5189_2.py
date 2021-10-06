# def f(i, k):
#     if i == k: # 경로 한개 완성
#         # s = bat[0][A[0]]  # 사무실 -> 첫 경유지 가는데 드는 배터리 소비량
#         s = 0
#         for j in range(k-1): # 경유지의 출발 인덱스        # 경유지 사이의 비용
#             # k - 도착, k-1 경유, k-2 출발지
#             s += bat[A[j]][A[j+1]]
#         s += bat[A[k-1]][A[0]]  # 마지막 경유지 -> 사무실로 이동하는 배터리 소비량
#         print(s)

# def f2(i, k, s):  # 경유지가 나올때마다 배터리소모량 더해서 확인
#     global minV
#     if i == k:  # 경로 한개 완성
#         s += bat[A[k-1]][0] # 마지막 경유지 -> 사무실
#         if s < minV:
#             minV = s
#     else:
#         for j in range(i, k):
#             A[i], A[j] = A[j], A[i] # A[j]에 있는게 도착지 번호 # 이번에 고를게 A[i]
#             f2(i+1, k, s + bat[A[i-1]][A[i]])
#             A[i], A[j] = A[j], A[i]
#
#
# A = [0, 1, 2, 3]
# for tc in range(1, int(input())+1):
#     n = int(input())
#     bat = [list(map(int, input().split())) for _ in range(n)] # 배터리 소비량
#     A = [a for a in range(n)]
#     s = 0  # 사무실까지 오는데 오는 배터리 소모량은 0 이니 0을 넘겨주기
#     minV = 100*10
#     f2(1, n, s)  # 0번인덱스는 고정이니, 1번부터 만드는데 총 4개짜리. (n개)
#     print(f'#{tc} {minV}')

# 민형님 풀이
# 메모리 값이 크지 않을 때에는 itertools
# from itertools import permutations, combinations
# 비투마스킹


def func(now, tmp, i):  # tmp -> 연료값을 추가하기 위한 변수
    global res
    if i == n - 1:
        tmp += battery[now][0]
        res = min(res, tmp)
    elif tmp > res:
        return
    else:
        for idx in range(1, n):  # 1은 고정이기 때문에 그 다음부터 돌린다
            if not visited[idx]:
                visited[idx] = 1
                func(idx, tmp + battery[now][idx], i + 1)  # 백트래킹
                # 연료값 추가하기 위해서 tmp + 로,
                visited[idx] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    battery = [list(map(int, input().split())) for _ in range(n)]

    res = 100 * n
    visited = [0] * n
    visited[0] = 1
    func(0, 0, 0)
    print(f'#{tc} {res}')



