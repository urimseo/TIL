'''
퍼펙트 셔플
p1 -> 시작점, p2 -> 중간부터
개수가 다를 수 있으니 p2

'''
# for tc in range(1, int(input())+1):
#     n = int(input())
#     card = list(input().split())
#
#     if n %2 ==0:
#         card1 = card[0:n//2]
#         card2 = card[n//2 : n]
#     else:
#         card1 = card[0:n//2+1]
#         card2 = card[n//2+1: n]
#     total = []
#     while n!=0:
#         if card1:
#             total.append(card1.pop(0))
#             n-=1
#         if card2:
#             total.append(card2.pop(0))
#             n-=1
#     print(f'#{tc}', end=' ')
#     print(*total)

# 인덱스 연산으로 해보기
# n = int(input())
# card = list(input().split())
# pos1 =전반부 시작
# pos2 = 후반부 시작
# 반복 횟수  =>