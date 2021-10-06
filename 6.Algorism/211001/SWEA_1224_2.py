def f(i, n, c):
    global maxV
    global maxC
    if c == 0 or i == n : # 교환횟수가 0이거나 기준위치가 맨 오른쪽 카드가지 고려된 경우
        # 현재 숫자판 순서로 최대값과 비교
        # 기존의 최대값과 같으면 교환횟수가 큰 쪽을 선택
        s = 0 # 카드의
        for x in card:
            s = s*10 + x
        if maxV <= s:
            maxV = s
            if maxC > c:
                maxC = c
        # if maxV < s:
        #     maxV = s
        #     maxC = c
        # elif maxV == s and maxC > c: # 더 많은 교환횟수를 사용한 경우를 선택
        #     maxC = c

    else:
        for j in range(n):
            if i != j:
                card[i], card[j] = card[j], card[i]
                f(i+1, n, c-1)
                card[i], card[j] = card[j], card[i]  # 원상복구..
                # 기준위치만 바꾸고 교환 없는 호출
                f(i+1, n, c)





for tc in range(1, int(input())+1):
    num, cnt = input().split()
    card = list(map(int, num))
    maxV = 0                  # 최대상금
    maxC = 0                  # 최대상금을 만들고 남은 교환횟수가 저장됨
    f(0, len(card), int(cnt)) # 교환 기준 위치 - 0번자리부터 시작, 숫자판 개수, 교환횟수
    print(maxV, maxC)