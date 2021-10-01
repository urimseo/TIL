'''
 최대상금
'''

c, n = map(int, input().split())
cards = []
for i in str(c):
    cards.append(int(i))
# card = [1, 2, 3]
cnt = 0 # 교환횟수
# 정렬..?
change = []
Len = len(cards)
for i in range(Len):
    tmpV = 0 # 최대값을 찾기 위한 임시 변수
    tmp = 0
    tmplst = cards[i+1:Len]
    for id, maxV in enumerate(tmplst):
        if maxV >= tmpV:
            tmpV = maxV
            idx = id + i + 1


    for j in range(i+1, Len):
        if cards[i] < tmpV:
            change.append([idx, cards[i]])
            cards[i], cards[idx] = cards[idx], cards[i]
            n -= 1
            if n == 0:
                break
    if n == 0:
        break
if n % 2 == 1: # 홀수이면
    cards[-1], cards[-2] = cards[-2], cards[-1]
print(cards)






