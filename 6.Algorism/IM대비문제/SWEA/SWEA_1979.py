for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    lst = [[0]*(n+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(n)] + [[0]*(n+2)]
    res = 0
    for i in range(n+2):
        cnt = 0
        cnt2 = 0
        for j in range(n+2):
            if lst[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    res += 1
                    cnt = 0
                else:
                    cnt = 0
            if lst[j][i] == 1:
                cnt2 += 1
            else:
                if cnt2 == k:
                    res += 1
                    cnt2 = 0
                else:
                    cnt2 = 0
    print('#{} {}'.format(tc, res))
