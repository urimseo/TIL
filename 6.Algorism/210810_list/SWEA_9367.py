t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 1
    maxV = 0
    newlst = lst + [0]
    for i in range(n):
        if newlst[i+1]-newlst[i] == 1:
            cnt += 1
        else:
            if cnt > maxV:
                maxV = cnt
                cnt = 1
    if cnt > maxV:
        maxV = cnt
    print(f'#{tc} {maxV}')