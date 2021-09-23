'''
if i+j == k or (i+j) % k == 0  토글
m이 k의 배수인 경우, or m초에는 전체 토글
'''
for tc in range(1, int(input())+1):
    n, m  = map(int, input().split())
    lst = [list(map(int, input().split()))for _ in range(n)]

    for k in range(1, m+1):# k는 1 2 3 .으로 증가
        for i in range(1, n+1):
            for j in range(1, n+1):
                if m % k == 0 or k == m:
                    if lst[i-1][j-1] == 1:
                        lst[i-1][j-1] = 0 # 이면 0으로
                    else: # 0이면 1로 토글
                        lst[i-1][j-1] = 1

                else:
                    if i+j == k or (i+j)%k == 0:
                        if lst[i-1][j-1] == 1:
                            lst[i-1][j-1] = 0
                        else:
                            lst[i-1][j-1] = 1
    cnt = 0
    for r in range(n):
        for c in range(n):
            if lst[r][c] ==1:
                cnt += 1
    print(f'#{tc} {cnt}')