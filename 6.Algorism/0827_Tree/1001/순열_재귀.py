'''
def perm(n, k):
    if k ==n:
        print(p)
        return
    else:
        for i in range(k, n):
            p[k], p[i] = p[i], p[k]
            perm(n, k+1)
            p[k], p[i] = p[i], p[k]
p = [1, 2, 3]
perm(3, 0)
'''
# def f(n, k):
#     if n == k:
#         print(p)
#     else:
#         for i in range(n): # u를 앞에서부터 뒤지기
#             if u[i] == 0:  # 가장작은자리부터 쓰지 않은 u를 뒤져
#                 u[i] == 1 # u를 사용처리하고
#                 p[k] = arr[i] # p에다가 넣기
#                 f(n, k+1) # 다시 k증가시켜서 함수 호출?
#                 u[i] = 0 # u 초기화
#
# p = [0]*3   # 빈배열 만들기
# arr = [1, 2, 3] # 사용할 숫자
# u = [0]*3 # 사용했는지 확인할 used 배열
# f(3, 0)


# 5개중에 3개 고르기 (5*4*3)
def f(n, m, k):
    if n == k:
        print(p)
    else:
        for i in range(m): # u를 앞에서부터 뒤지기
            if u[i] == 0:  # 가장작은자리부터 쓰지 않은 u를 뒤져
                u[i] = 1 # u를 사용처리하고
                p[k] = arr[i] # p에다가 넣기
                f(n, m, k+1) # 다시 k증가시켜서 함수 호출?
                u[i] = 0 # u 초기화

p = [0]*3   # 빈배열 만들기
arr = [1, 2, 3, 4, 5] # 사용할 숫자
u = [0]*5 # 사용했는지 확인할 used 배열
f(3, 5, 0)