''' 테스트케이스 3개 틀림..!

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))

    cnt = 0  # 1의 개수 세기
    if 1 in numbers:  # 1이 하나라도 있으면 1부터 시작
        cnt = 1
    res = 0 # 가장 큰 연속된 개수
    for i in range(N):
        if numbers[i] == 1 and i != N-1 and numbers[i+1] == 1: # 현재 인덱스의 값이 1이고, 다음 인덱스의 값도 1이면 +1
            cnt += 1
            if i != N-2 and numbers[i + 2] == 0:  # 다다음 인덱스가 0이면 연속된 값 끝, 최종적으로 연속된 수 저장
                res = cnt
                cnt = 1  # 일단 1이 있으니 다시 cnt가 1부터 시작해야 함. 다음 인덱스부터 cnt 하기 때문
    if res < cnt: # 연속된 수 중 큰 수 비교하여 저장
        res = cnt

    print(f'#{tc} {res}')
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))

    cnt = 0  # 1의 개수 세기
    res = 0 # 가장 큰 연속된 개수
    for i in range(N):
        if numbers[i] == 1: # 현재 인덱스의 값이 1
            cnt += 1
        else:
            if res < cnt:  # 연속된 수 중 큰 수 비교하여 저장
                res = cnt
                cnt = 0
    if res < cnt: # 마지막까지 1이 연속으로 있을경우에는 반복문 나와서 비교
        res = cnt
    print(f'#{tc} {res}')


''' 재연님 정답 코드  -> string으로 접근
T=int(input())
for tc in range(T):
        N = int(input())
        num=input()
        res, cnt=0, 0
        for i in num:
            if i=='1':
                cnt+=1
            else:
                if cnt>res:
                    res=cnt
                    cnt=0
        if cnt>res:
            res=cnt
        print(f"#{tc+1} {res}")
'''