t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))

    #버블정렬
    # for i in range(n-1, -1, -1): # 범위의 끝을 줄여주기 위함
    #     for j in range(0, i): # 줄어든 범위내에서
    #         if num[j] > num[j+1]: # 가장 큰걸 맨 뒤로
    #             num[j], num[j+1] = num[j+1], num[j]
    #
    # print(num)

    # 