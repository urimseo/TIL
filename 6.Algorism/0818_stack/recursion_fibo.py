# 재귀
#
# def f(i, k):
#     if i == k:  # 배열을 벗어나면 ( 모든 원소에 대한 작업이 끝나면 )
#         return
#     else:
#         print(A[i])
#         f(i+1, k)  # 다음 원소로 이동
#
# N = 3
# A = [10, 20, 30]
# f(0, N)
#
# fibonacci
# def fibo(n):
#     global cnt
#     cnt += 1
#     if n < 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# cnt = 0
# print(fibo(20), cnt)

# memo

def fibo2(n):
    if n >2 and memo[n] == 0:
        memo[n] = fibo2(n-1) + fibo2(n-2)
    return memo[n]


n = 50
memo = [0] * (n+1) # 인덱스 값을 그대로 쓰기 위해서 하나 더 만듬. 1~50
memo[0] = 0
memo[1] = 1
print(fibo2(n))