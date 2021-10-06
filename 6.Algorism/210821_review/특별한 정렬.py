t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(0, n, 2):
        minV = i+1
        maxV = i
        for j in range(i, n): # i는 2칸씩 정렬된거 다음부터 탐색
            if lst[maxV] < lst[j]: # 최대값
                lst[maxV], lst[j] = lst[j], lst[maxV]
            if lst[minV] > lst[j]: # 최소값
                lst[minV], lst[j] = lst[j], lst[minV]
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(lst[i], end=' ')
    print()

