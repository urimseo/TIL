
# [0 0 3 5 2 4 9 0 6 4 0 6 0 0]  # N = 14

for T in range(10):
    N = int(input())
    Building = list(map(int, input().split()))
    total = 0 #  최종 print

    for i in range(2, N-2): # i = 3 임 첫번쨰는  두번쨰는 i = 5

        floor = Building[i]  # 현재의 중간 층 수  # i =2, 3가리킴 # i = 3, 5가리킴
        MaxB = Building[i-2:i] + Building[i+1:i+3]   # 중간층수를 제외한 리스트 총 4개
        maxb = 0
        for k in MaxB:
            if k > maxb:
                maxb = k

        if floor - maxb > 0:
            tmp = floor - maxb
            total += tmp
    print(f'#{T+1} {total}')






