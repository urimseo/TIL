
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    lst = [list(input()) for _ in range(n)]
    res = []
    res2 =[]
    flag = 0
    r = 0
    while r < n and flag == 0:
        for i in range(n-m+1): #열 길이 자르기
            res = []
            res2 = []
            for j in range(i, i+m):
                res.append(lst[r][j])
                res2.append(lst[j][r])
            if res == res[::-1]:
                flag = 1
                break
            if res2 == res2[::-1]:
                flag = 2
                break
        r += 1
    if flag == 1:
        print('#{} {}'.format(tc, ''.join(res)))
    elif flag == 2:
        print('#{} {}'.format(tc, ''.join(res2)))

