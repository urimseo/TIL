for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    total = 0
    # 큰수 k개 찾아서 더하기
    for i in range(k):
        maxV = 0
        for s in score:
            if s > maxV:
                maxV = s
        total += maxV
        score.remove(maxV)
    print('#{} {}'.format(tc, total))
