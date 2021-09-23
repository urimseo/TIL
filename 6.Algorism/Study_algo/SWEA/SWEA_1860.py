'''
진기의 붕어빵
0초 ~ M 초 -> k개 붕어빵
0초 이후 손님들이 도착하는 시간이 주어지면, 기다리는 손님 없이 붕어빵 제공 가능 불가능?


'''
for t in range(1, int(input())+1):
    n, m, k = map(int, input().split()) # 사람수, 초, 붕어빵개수
    arrive = list(map(int, input().split())) # 사람오는 시간
    mission = ['Possible', 'Impossible']
    res = -1  # 성공 판단
    arrive.sort()
    # 일단 도착 초 정렬하기
    guest = 0  # 손님
    bread = 0  # 빵
    for i in range(n):
        guest += 1 # 온 손님
        bread = (arrive[i]//m)*k  # 빵의수
        if bread - guest >= 0: # guest > bread :
            res = 0
        else:
            res = 1
            break
    print(f'#{t} {mission[res]}')