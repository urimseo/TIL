'''
회문2
T = 10
100 * 100 정사각형
글자는 ABC중 하나
회문은 직선만 인정
가장 긴 회문의 길이 출력
'''

# for tc in range(1, 11):

# print(varr)
# n = 100 # 회문 길이 -> 점점 줄어들어야함
# while n > 0:
#     for i in range(100):
#         for j in range(100-j):
#             tmp = arr[i][j:j+n]  # 가로탐색  m 만큼 슬라이싱
#             tmp2 = varr[i][j:j+n]
#             if tmp == tmp[::-1]:
#                 res = n
#                 break
#             elif tmp2 == tmp[::-1]:
#                 res2 = n
#                 break
#         n -= 1


for tc in range(1, 11):
    T = int(input())
    arr = [list(input())for _ in range(100)]
    varr = list(zip(*arr[::-1])) # 세로 리스트
    res = '' # 0 이 아닌 시점에 break len(res) != 0 -> break

    for m in range(100, 0, -1): # 회문의 길이 줄어들면서 99 ~ 0 까지
        # 길이까지 하려면 m 함수로 return ...
        for i in range(100):  # 행 탐색 * 100
            for j in range(100-m+1):  # 열 탐색 100인데 처음엔 100 그 다음엔 m 줄어들어서 99...
                tmp = arr[i][j:m+j]  # 가로탐색  m 만큼 슬라이싱
                tmp2 = varr[i][j:m+j]  # 세로탐색 m 만큼 슬라이싱
                if tmp == tmp[::-1]:  # 회문 탐색
                    res = tmp
                    break
                elif tmp2 == tmp2[::-1]:
                    res = tmp2
                    break
            if res:  # 빈 문자열이 아니면 True
                break
        if res:
            break
    print(f'#{T} {len(res)}')





            #
            #
            # cnt = 0
            # for j in range(m//2):  # 비교 횟수, or 비교 위치->(M//2 -1)
            #     if str1[i][m+j] == str1[i][m+-1-j]: # 모든 경우를 다 비교하게 됨. 일치하게되면 안쪽도 비교하기 때문..?
            #         cnt += 1
            #
