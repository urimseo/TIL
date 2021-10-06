'''
수영장
- 완전탐색
1일, 1달, 3달
- 가장 적은 비용 출력
'''

def f(n, s): # n월 , s 이전까지의 비용
    global minV
    if n > 12:  # 모든 달에 대한 고려가 끝 났으면
        if minV > s:
            minV = s
    elif minV < s: return  # 중간에 이미 1년권보다 금액이 비싸면 return
    else:
        # 1개월치만 결제하는 경우
        f(n+1, s+min(swim[n]*price[0], price[1]))  # n월에 1개월치만 결제하는 경우
        f(n+3, s+price[2])  # n월에 3개월 이용권을 결제하는 경우

# 처음함수에 들어오면 f(n+1~~) 여기만 쭉 호출이 되면서 f1 ~12 까지의 1일권, 1개월권 중 저렴한 금액권이 선택됨.
# f13이 되면 if 문에 걸려서 minV와 비교를 하게됨. minV 보다 작을 경우 1일권, 1개월권만 사용하는 금액이 우선 채택된다.
# 그 다음은 3개월권을 탐색f(n+3~~)
# n = 12 + 3 이기 때문에 15가 된다. 그럼 다시 if문에 걸려서 minV 를 탐색. (첫번쨰 tc의 경우 210이 됨 -> 이럴 경우 그냥 12월 권 + 3개월권이 더해지는 것이니 당연히 클수밖에 없지..)
# n이 12 ~ 1 로 줄면서 +3 을하며 return하면서 비교된다.


for tc in range(1, int(input())+1):
    price = list(map(int, input().split()))
    swim = [0] + list(map(int, input().split()))  # 1~12월을 인덱스로 사용
    minV = price[3]  # 1년치 이용권을 초기비용으로 설정하여 함수 안에서 이것보다 가격이 적으면 됨.
    f(1, 0)
    print(f'#{tc} {minV}')

############################################
def cost(m, s):  # m은 월, c는 합할 금액
    # 탈출 조건부터 만들기
    global minV
    if m > 12:
        if minV > s:
            minV = s
    else:
        cost(m + 1, s + swim[m] * day) # 일금액 계산
        cost(m + 1, s + m1) # 월금액 계산
        cost(m + 3, s + m3) # 3개월 금액 계산


for tc in range(1, int(input()) + 1):
    day, m1, m3, year = map(int, input().split())
    swim = [0] + list(map(int, input().split()))
    minV = year  # 최소 금액을 1년치로 잡아.

    cost(1, 0)  # m은 월, c는 합할 금액
    print(f'#{tc} {minV}')

##################################################


''' # 라이브 풀이 
# cost: 이전 달까지의 계산 결과, m: 현재 내가 보낼 결과
def calc(cost, m): # 비용, 몇번째 달인지 m
    global min_cost
    if m > 12: # 12월까지 계산을 하고 넘겨야함.
        if min_cost < cost:
            min_cost = cost
            return
    # # 1일권
    # calc(cost + d*month[m], m+1)
    # # 1달권
    # calc(cost + m1, m+1)
    # 1일권과 1달권을 한번에 처리
    calc(cost + min(d*month[m], m1), m+1)
    # 3달권
    calc(cost + m3, m + 3)


for tc in range(1, int(input())+1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    min_cost = y # 1년치 비용이 현재 최저의 가격

    calc(0, 1)
    print(f'#{tc} {min_cost}')


#dp풀이###############################################################
'''

'''
for tc in range(1, int(input())+1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    min_cost = y # 1년치 비용이 현재 최저의 가격

    dp = [0] * 13 # 해당 월까지의 최소값이 저장이 되어 있음

    dp[1] = min(m1, month[1]*d) # 1월
    dp[2] = dp[1] + min(m1, month[2]*d)

    for i in range(3, 13):
        dp[i] = min(dp[i-3]+m3, dp[i-1]+m1, dp[i-1]+ month[i]*d) # 3달치 요금, 전달 요금 + 1달치, 전달 요금 + 일일권
'''



















