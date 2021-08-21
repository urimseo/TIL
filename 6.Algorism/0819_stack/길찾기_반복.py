'''
#입력 받기

1. 홀/짝으로 받기
2. 2step
for i in range(0, len(road),2):
    i, i+1을 하나에 담기
3. 2*
for i in range(n) # 0~n-1까지 반복
    2*i, 2*i+1 (0, 0+1), (2, 3)... 과 같이 증가 가능

# 저장하기
1. ch1, ch2
ch1 = [0] *100
ch2 = [0]*100

#인접행렬
    # for i in range(N):
    #     st = road[2*i]
    #     ed = road[2*i+1]
    #
        ##저장방법
        # ch1, ch2 -> 최대 길의 개수가 2개이기 때문
    # ch1 = [0]* 100
    # ch2 = [0] * 100
    # for i in range (N):
    #     if ch1[road[2*i]] == 0:  # 인덱스 -> 시작점, 데이터는 도착점
    #         ch1[road[2*i]] = road[2*i+1]
    #     else:
    #         ch2[road[2*i]] = road[2*i+1]
    # # 2. 인접행렬 방식
    # adj_arr = [[0] * 100 for _ in range(100)]
    # for i in range(N):
    #     adj_arr[road[2*i]][road[2*i+1]] = 1
'''

for _ in range(1):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))


    # 3. 인접 리스트 방식
    adj_list = [[] for i in range(100)]
    for i in range(N):
        adj_list[road[2*i]].append(road[2*i+1])

    visited = [0]* 100
    ans = 0
    stack = [0]
    while stack:
        curr = stack.pop()

        if curr == 99:
            ans = 1
            break
        # 방문하지 않았으면 -> 각자 작성
        # 방문을 했으면 건너가
        if visited[curr]:
            continue
        visited[curr] = 1

        for w in adj_list[curr]:
            if not visited[w]:
                stack.append(i)

    print(f'#{tc} {ans}')