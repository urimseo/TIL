'''
동철이의 일 분배
1. used 배열 운용
2. max_mul 을 이용해서 가지치기
-> 곱하면 곱할수록 확률을 줄어든다.
'''

def work(i, percent):
    global res
    if i == n:
        res = max(res, percent)
        return res
    elif res >= percent:
        return

    else:
        for j in range(n):
            if used[j]: continue
            used[j] = 1
            work(i+1, percent*lst[i][j]*0.01)
            used[j] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    used = [0] * n
    res = 0
    work(0, 1)
    print('#{} {:.6f}'. format(tc, res*100))