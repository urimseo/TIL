'''
화물 도크
0시~ 다음날 0시 전까지
최대한 많은 화물차가 화물을 싣고 내릴 수 있다.
최대 몇대의 화물차가 이용할 수 있는가.

작업시작 시간 - 완료 시간 ( 정각 기준)
앞작업의 종료 + 다음 작업 시작
5
20 23 - 작업시작 s , 종료시간 e
17 20
23 24
4 14
8 18
'''
for tc in range(1, int(input())+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    end = sorted(lst, key=lambda x : x[1])

    cnt = 1
    s = end[0][0]  # 시작시간
    e = end[0][1]  # 종료시간

    for j in range(n):
        if end[j][0] >= e:  # 시작시간이 종료시간 뒤에 있으면
            s = end[j][0]
            e = end[j][1]
            cnt += 1
    print(f'#{tc} {cnt}')




# for tc in range(1, int(input())+1):
#     n = int(input())
#     lst = [list(map(int, input().split())) for _ in range(n)]
#     start = sorted(lst, key=lambda x : x[0])
#     end = sorted(lst, key=lambda x : x[1])
#
#     cnt = 0
#     s = 0  # 시작시간
#     e = 0  # 종료시간
#     while e != end[-1][1]:
#         for i in range(n):
#             if e <= end[i][0]: # 종료시간보다 나의 시작시간이 느리면?
#                 e = end[i][1]
#                 s = end[i][0]
#                 cnt += 1
#                 break
#         for j in range(n):
#             if start[j][0] >= e: # 시작시간이 종료시간 뒤에 있으면
#                 s = start[j][0]
#                 e = start[j][1]
#                 cnt += 1
#                 break
#     print(f'#{tc} {cnt}')