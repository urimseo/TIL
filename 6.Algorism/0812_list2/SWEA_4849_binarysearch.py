'''
이진탐색

책 페이지수는 동일
a, b 두사람 -> 각자 찾을 쪽 번호 다름
먼저 찾는 사람이 이김

이긴사람 출력, 비겼으면 0 출력
'''
'''
B - 책 페이지 수 들어있는 리스트 1`400까지
cnt - 찾은 횟수 count
p - 전체 페이지
ap - a가 찾아야할 페이지
b - b가 찾아야할 페이지
'''
T = int(input())
def Page_search(B, k, p):
    start = 1
    end = p
    cnt = 0
    while start <= end:
        middle = (start + end) // 2
        cnt += 1
        if B[middle - 1] == k:
            return cnt
        elif B[middle - 1] > k:
            end = middle
        else:
            start = middle
for tc in range(1, T+1):
    p, ap, bp = map(int, input().split())
    B = list(range(1, p+1))
    # 페이지 나눈 수만큼을 각각 저장
    totala = Page_search(B, ap, p)
    totalb = Page_search(B, bp, p)

    if totala < totalb:
        winner = 'A'
    elif totala > totalb:
        winner = 'B'
    else:
        winner = 0
    print(f'#{tc} {winner}')









# for i in Book: #
#     while sta <= fina:
#         mida = (sta + fina) //2
#         cnt_a += 1
#         if Book[mida-1] == ap:
#             total_a = cnt_a
#         elif Book[mida-1] > ap:
#             fina = mida
#         else:
#             sta = mida



# for i in Book:
#     while sta <= fina:
#         mida = (sta + fina) // 2
#         cnt_a += 1
#         if Book[mida] == ap:
#             total_a = cnt_a
#         elif Book[mida] > ap:
#             fina = mida
#         else:
#             sta = mida
#
#     else:
#         total_a = 0