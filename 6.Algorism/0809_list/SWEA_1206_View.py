
# [0 0 3 5 2 4 9 0 6 4 0 6 0 0]  # N = 14

for T in range(10):
    N = int(input())
    Building = list(map(int, input().split()))
    total = 0 #최종 print
    maxV = 0 # 최댓값을 찾기
    for i in range(2, N-2): # i = 3 임 첫번쨰는  두번쨰는 i = 5

        floor = Building[i]  # 현재의 중간 층 수  # i =2, 3가리킴 # i = 3, 5가리킴
        MaxB = Building[i-2:i+3]  # 5개씩 끊어서 보기
        maxb = max(MaxB)
        new_list = list(range(i-2, i))+list(range(i+1, i+3))
        MaxB2 = Building[i-2:i] + Building[i+1:i+3]   # 중간값 제외한 리스트 총 4개
        maxb2 = max(MaxB2)

        if maxb - maxb2 > 0:
            tmp = maxb - maxb2
            total += tmp
    print(f'#{T+1} {total}')






