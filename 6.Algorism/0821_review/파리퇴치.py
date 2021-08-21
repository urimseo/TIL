
t = int(input())
for tc in range(1, t+1):

    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    maxp = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            res = 0
            for a in range(m):
                for b in range(m):
                    res += lst[i+a][j+b]
            if res > maxp:
                maxp = res
    print(f'#{tc} {maxp}')
#
# TC = int(input())
#
# for tc in range(TC):
#     # 1. input받아오기
#     N, M = map(int, input().split())
#     # N: 영역의 크기
#     # M: 파리채의 크기
#     # 2. arr만들기 / 변수명 소문자
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # print(arr)  #[[1, 3, 3, 6, 7], [8, 13, 9, 12, 8], [4, 16, 11, 12, 6], [2, 4, 1, 23, 2], [9, 13, 4, 7, 3]]
#
#     """
#     1. N 영역을 위한 for문 2개 (i, j)
#         for i: 0 -> N-M+1
#           for j: 0 -> N-M+1
#
#             2. M영역을 위한 for문 2개 (rm, cm)
#                 for i: 0 -> M-1
#                     for j: 0 -> M-1
#     """
#     # 4. max_sum = 0 (마이너스 파리는 없으므로)
#     max_sum = 0
#     for i in range(N - M + 1):
#         for j in range(N - M + 1):
#             # 5. 한 파리채 크기만큼 돌았을 때,
#             temp_max_sum = 0
#             for rm in range(M):
#                 for cm in range(M):
#                     temp_max_sum += arr[i + rm][j + cm]  # 4번계산.
#                     # print(arr[i + rm][j + cm])
#             # 5. 어펜드 대신 이 방법. 그때그때의 max구해가면서
#             # print(temp_max_sum)
#             if temp_max_sum > max_sum:
#                 max_sum = temp_max_sum
#
#     # print(max_sum)
#     print(f'#{tc + 1} {max_sum}')
