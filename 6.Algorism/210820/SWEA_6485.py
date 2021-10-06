'''
삼성시의 버스노선
5000 -> 버스 정류장의 수
N -> 버스노선의 개수

'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # [[1, 3], [2, 5]]  a1, b1 / a2, b2 = bj
    P = int(input())

    stations = []  # 정류장
    for _ in range(P):
        stations.append(int(input()))
    # [1, 2, 3, 4, 5]
    dicta = {}  # 정류장(키) 마다 갈 수있는 노선 수를 value에 추가
    a = []
    for j in lst: # 버스가 지나지 않는 정류장이생기지 않는다.
        for i in range(j[0], j[1]+1):
            if i not in dicta:
                dicta[i] = 1
            else:
                dicta[i] += 1
    stop = [] # 값만 따로 저장
# station이 지나지 않는 버스정류장도 출력하라고 함
    # 버스가 서지 않는 정류장도 생긴다. 그럴 경우 0을 찍어야함.
    for i in stations:
        if i in dicta:
            stop.append(dicta[i])
        else:
            stop.append(0)

    print(f'#{tc}', end=' ')
    for i in range(P):
        print(stop[i], end=' ')
    print()


    #
    # print(f'#{tc}', end=' ')
    # for i in stations:
    #     print(dicta[i], end=' ')
    # print()
    #

#1 1 2 2 1 1

#2 2 4 4 2 2
