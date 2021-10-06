'''
종이붙이기 -> Tiling 문제
재귀 or dp로 가능.
10으로 나눠서 검사 시작!
basecase 만들기 f(0), f(1) f(2)
1. 재귀 : 반복호출 f(n) = f(n-1) + 2f(n-2)
2. dp : 배열에 저장해서 인덱스로 접근
'''
# dp 풀이
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input()) // 10
#     memo = [0] * (n+1)
#     memo[0] = 1
#     memo[1] = 1
#     memo[2] = 3
#
#     for i in range(1, n+1):
#         memo[i] = memo[i-1] + 2*memo[i-2]
#
#     print(f'#{tc} {memo[n]}')



# 재귀 풀이

def tiling(n):
    # base case
    if n == 2:
        return 3
    elif n == 1:
        return 1
    # recursion
    else:
        return tiling(n-1) + 2*tiling(n-2)

T = int(input())
for tc in range(1, T+1):
    n = int(input()) // 10
    print(f'#{tc} {tiling(n)}')
