T = int(input())

for tc in range(T):
    N = list(map(int, input().split()))
    n = len(N)
    ans = 0  # 합이 0 이 나오면 1, 아니면 0으로 남아있게된다.
    for i in range(1, 1 << n + 1):  # (2^N) 1~ 2^10 까지  0부터 이면 공집합, +1 을 해줘야 1024까지 간다. 아니면 1023까지.
        total = 0
        for j in range(n): # 각각의 자리수를 확인한다.
            if i & (1 << j):  # j번 bit 가 1인 값, 10, 10, 100으로 밀면서 확인한다.
            # 1을 j 만큼 민다.
                total += N[j]

        if total == 0:
            ans = 1
            break  # 부분집합의 합이 0인게 있으면 중단

        # if not total:
        #     ans = 1
        #     break

        # if j != n-1 and total != 0: # 아니면 0을 출력해야 하는데, 부분집합의 마지막 까지 봐야하니까 마지막?
        #     print(f'#{tc + 1} 0')
        # 이렇게 할 필요가 없다!!!!
        # 합에 0이 나온적이 없으면 기본 ans = 0이니까 그걸 출력하면 된다.
    print(f'#{tc+1} {ans}')
