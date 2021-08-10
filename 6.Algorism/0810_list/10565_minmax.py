T = int(input())

for tc in range(1, T+1):
    N = int(input())
    LIST = list(map(int, input().split()))

    maxV = LIST[0]
    minV = LIST[0]
    result = 0
    for i in LIST:  # range(N-1)로 굳이..?
        if maxV < i:
            maxV = i

        if minV > i:
            minV = i
    result = maxV - minV
    print(f'#{tc} {result}')


'''
# for 문을 N번, N번 따로 돌면 연산회수 2N
    # for 문 안에 if 2번이 좋다. 
    # if 조건을 만족하면 두번째 elif를 실행하지 않아, 
    # it 두번보다 빠르다. 
'''






