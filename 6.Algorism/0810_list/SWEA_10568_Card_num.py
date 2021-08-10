T = int(input())

for tc in range(T):
    N = int(input())
    number = list(map(int, (input())))
    cnt = [0]*10 # 0부터 9까지의 카운트

    # cnt 인덱스에 카드 숫자만큼 넣기 카운드 배열 만들기
    for i in range(0, N):
        cnt[number[i]] += 1

    # 가장 큰 숫자가 들어있는 자리
    m_idx = 0
    for i in range(1, len(cnt)):
        # 현재까지 가장 큰 수보다, 뒤에 있는 인덱스에 있는 수가 더 크면~
        # 가장 큰 수가 같을때는 더 큰 수를 골라야 한다.
        # 그러므로, 같을 때는 m_idx 에 더 큰 i 를 넣어야 하기 때문에
        # 나중에 나온 숫자로 바꿔주면 된다.
        # < 가 아닌 <=
        if cnt[m_idx] <= cnt[i]:
            m_idx = i

    print(f'#{tc+1} {m_idx} {cnt[m_idx]}')