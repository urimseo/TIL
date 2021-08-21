'''
백만장자 프로젝트
    1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    3. 판매는 얼마든지 할 수 있다.

- 팔 수 있는지 없는지 체크!
뒤에 보다가 나보다 큰 값이 나오면 사도 되는거임
살 수 있으면 cost += 값, cnt += 1


3
10 7 6
'''
#
# days = int(input()) # 예측날짜
# prices = list(map(int, input().split())) # 가격


# 최댓값 구하기...


days = 5
prices = [1, 1, 3, 1, 2]
res = 0  # 산 금액
cnt = 0  # 산 수량

newlst = []
maxidx = -1
while maxidx != len(prices):
    maxp = 0
    for i in range(maxidx +1, len(prices)):
        if prices[i] > maxp:
            maxp = prices[i]
            maxidx = i

    for j in range(0, maxidx):
        if prices[j] < prices[maxidx]:
            res += prices[j]
            cnt += 1

    if maxidx != len(prices):
        newlst = prices[maxidx+1:len(prices)]
        print(newlst)









