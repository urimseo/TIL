t = int(input())
for tc in range(1, t+1):

    lst = list(map(int, input().split()))
    # subset = [[]]
    # for i in lst:
    #     size = len(subset)
    #     for j in range(size):
    #         subset.append(subset[j] + [i])
    # subset.pop(0)
    # # 공집합 없애기
    # # b = [i for i in subset[1:]]
    #
    # sumlst = []
    # for i in subset:
    #     res = 0
    #     for j in i:
    #         res += j
    #     sumlst.append(res)
    # total = 0
    # if 0 in sumlst:
    #     total = 1
    #
    # print(f'#{tc} {total}')

    n = len(lst)
    total = []
    for i in range(1, 1<<n):
        arr = []
        for j in range(n):
            if i & (1<<j):
                arr.append(lst[j])
        total.append(arr)

    print(total)