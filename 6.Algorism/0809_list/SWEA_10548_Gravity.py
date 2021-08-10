T = int(input()) # 테스트 케이스 개수
for tc in range(1, T+1):

    N = int(input()) # 방의 가로 길이
    A = list(map(int, input().split())) # 상자의 높이

    maxV = 0
    for i in range(N-1):          # N-1 = 9 첫번쨰 i = 7
        cnt = 0
        for j in range(i+1, N):    # 7 4 2 0 0 6 0 7 0  => 4부터 0까지
            if A[i] > A[j]:        # A[i] 0 = 7. A[j] 1 = 4
                cnt += 1           # cnt = 1
        if maxV < cnt:             # maxV = cnt
            maxV = cnt
    print(f'#{tc} {maxV}')



        # cnt를 for i 문에 넣어주면 초기화 시키지 않아도됨.
        #     cnt = 0               # cnt 초기화 -> 그래야 누적되지 않음!
        # else:
        #     cnt = 0
